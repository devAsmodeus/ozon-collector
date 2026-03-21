"""Базовый HTTP-клиент для Ozon Seller API."""
import logging
import time

import httpx

from src.config import settings
from src.exceptions import (
    OzonApiException,
    OzonApiRateLimitException,
    OzonApiUnauthorizedException,
)
from src.metrics import (
    ozon_api_errors_total,
    ozon_api_rate_limits,
    ozon_api_requests_total,
    ozon_api_response_time,
)

logger = logging.getLogger(__name__)

_TIMEOUT = 30.0
_MAX_RETRIES = 3
_RATE_LIMIT_PAUSE = 60


class OzonApiClient:
    """Async HTTP-клиент для Ozon Seller API с retry и rate-limit handling."""

    def __init__(self, base_url: str | None = None):
        self.base_url = base_url or settings.OZON_API_BASE_URL
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Client-Id": settings.OZON_CLIENT_ID,
                "Api-Key": settings.OZON_API_KEY,
                "Content-Type": "application/json",
            },
            timeout=_TIMEOUT,
        )
        return self

    async def __aexit__(self, *args):
        if self._client:
            await self._client.aclose()

    async def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict | None = None,
        params: dict | None = None,
    ) -> dict:
        last_exc: Exception | None = None

        for attempt in range(1, _MAX_RETRIES + 1):
            start = time.monotonic()
            try:
                resp = await self._client.request(
                    method, path, json=json, params=params,
                )
                elapsed = time.monotonic() - start

                ozon_api_requests_total.labels(endpoint=path, method=method).inc()
                ozon_api_response_time.labels(endpoint=path).observe(elapsed)

                if resp.status_code == 200:
                    return resp.json()

                if resp.status_code == 401 or resp.status_code == 403:
                    ozon_api_errors_total.labels(endpoint=path, error_type="unauthorized").inc()
                    raise OzonApiUnauthorizedException(
                        resp.status_code, resp.text[:200],
                    )

                if resp.status_code == 429:
                    ozon_api_rate_limits.labels(endpoint=path).inc()
                    logger.warning(
                        "Rate limit hit, pausing %ds", _RATE_LIMIT_PAUSE,
                        extra={"endpoint": path, "attempt": attempt},
                    )
                    if attempt < _MAX_RETRIES:
                        import asyncio
                        await asyncio.sleep(_RATE_LIMIT_PAUSE)
                        continue
                    raise OzonApiRateLimitException(429, "Rate limit exceeded")

                ozon_api_errors_total.labels(endpoint=path, error_type=f"http_{resp.status_code}").inc()
                raise OzonApiException(resp.status_code, resp.text[:200])

            except (httpx.TimeoutException, httpx.ConnectError) as exc:
                elapsed = time.monotonic() - start
                ozon_api_errors_total.labels(endpoint=path, error_type="network").inc()
                last_exc = exc
                logger.warning(
                    "Network error (attempt %d/%d): %s",
                    attempt, _MAX_RETRIES, exc,
                    extra={"endpoint": path},
                )
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

    async def delete(self, path: str, *, json: dict | None = None) -> dict:
        return await self._request("DELETE", path, json=json)
