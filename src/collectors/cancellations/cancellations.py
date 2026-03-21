"""Коллектор: Отмены заказов."""
from src.collectors.base import OzonApiClient


class CancellationsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_list(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v2/conditional-cancellation/list — список запросов на отмену."""
        body = {"filter": filter or {}, "limit": limit, "offset": offset}
        return await self._client.post("/v2/conditional-cancellation/list", json=body)

    async def approve(self, *, cancellation_id: int) -> dict:
        """POST /v2/conditional-cancellation/approve — подтвердить отмену."""
        return await self._client.post("/v2/conditional-cancellation/approve", json={"cancellation_id": cancellation_id})

    async def reject(self, *, cancellation_id: int, reason: str = "") -> dict:
        """POST /v2/conditional-cancellation/reject — отклонить отмену."""
        return await self._client.post("/v2/conditional-cancellation/reject", json={
            "cancellation_id": cancellation_id, "reason": reason,
        })
