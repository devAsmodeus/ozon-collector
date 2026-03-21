"""HTTP-клиент для Ozon Performance API (реклама) — OAuth 2.0."""
import logging
import time

import httpx

from src.config import settings
from src.exceptions import OzonApiException, OzonApiRateLimitException
from src.metrics import (
    ozon_api_errors_total,
    ozon_api_rate_limits,
    ozon_api_requests_total,
    ozon_api_response_time,
)

logger = logging.getLogger(__name__)

_TIMEOUT = 30.0
_MAX_RETRIES = 3
_TOKEN_URL = "/api/client/token"


class OzonPerformanceClient:
    """Async HTTP-клиент для Ozon Performance API с OAuth 2.0 авторизацией."""

    def __init__(self):
        self.base_url = settings.OZON_PERFORMANCE_API_URL
        self._client: httpx.AsyncClient | None = None
        self._token: str | None = None
        self._token_expires_at: float = 0

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=_TIMEOUT,
        )
        await self._ensure_token()
        return self

    async def __aexit__(self, *args):
        if self._client:
            await self._client.aclose()

    async def _ensure_token(self) -> None:
        """Получает или обновляет OAuth токен."""
        if self._token and time.monotonic() < self._token_expires_at:
            return

        resp = await self._client.post(
            _TOKEN_URL,
            json={
                "client_id": settings.OZON_PERFORMANCE_CLIENT_ID,
                "client_secret": settings.OZON_PERFORMANCE_CLIENT_SECRET,
                "grant_type": "client_credentials",
            },
        )
        if resp.status_code != 200:
            raise OzonApiException(resp.status_code, f"Failed to get Performance token: {resp.text[:200]}")

        data = resp.json()
        self._token = data["access_token"]
        # Токен живёт 30 минут, обновляем за 60 сек до истечения
        self._token_expires_at = time.monotonic() + data.get("expires_in", 1800) - 60

    async def _request(self, method: str, path: str, *, json: dict | None = None, params: dict | None = None) -> dict:
        last_exc: Exception | None = None

        for attempt in range(1, _MAX_RETRIES + 1):
            await self._ensure_token()
            start = time.monotonic()
            try:
                resp = await self._client.request(
                    method, path, json=json, params=params,
                    headers={"Authorization": f"Bearer {self._token}"},
                )
                elapsed = time.monotonic() - start

                ozon_api_requests_total.labels(endpoint=f"perf:{path}", method=method).inc()
                ozon_api_response_time.labels(endpoint=f"perf:{path}").observe(elapsed)

                if resp.status_code == 200:
                    return resp.json()

                if resp.status_code == 429:
                    ozon_api_rate_limits.labels(endpoint=f"perf:{path}").inc()
                    if attempt < _MAX_RETRIES:
                        import asyncio
                        await asyncio.sleep(60)
                        continue
                    raise OzonApiRateLimitException(429, "Performance API rate limit")

                ozon_api_errors_total.labels(endpoint=f"perf:{path}", error_type=f"http_{resp.status_code}").inc()
                raise OzonApiException(resp.status_code, resp.text[:200])

            except (httpx.TimeoutException, httpx.ConnectError) as exc:
                ozon_api_errors_total.labels(endpoint=f"perf:{path}", error_type="network").inc()
                last_exc = exc
                if attempt < _MAX_RETRIES:
                    import asyncio
                    await asyncio.sleep(2 ** attempt)
                    continue

        raise OzonApiException(0, f"Max retries exceeded: {last_exc}")

    async def get(self, path: str, *, params: dict | None = None) -> dict:
        return await self._request("GET", path, params=params)

    async def post(self, path: str, *, json: dict | None = None) -> dict:
        return await self._request("POST", path, json=json)

    async def put(self, path: str, *, json: dict | None = None) -> dict:
        return await self._request("PUT", path, json=json)
