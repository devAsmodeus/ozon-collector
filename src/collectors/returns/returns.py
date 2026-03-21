"""Коллектор: Возвраты."""
from src.collectors.base import OzonApiClient


class ReturnsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_fbo_returns(self, *, filter: dict | None = None, limit: int = 100, last_id: int = 0) -> dict:
        """POST /v1/returns/list — список FBO возвратов."""
        body = {"filter": filter or {}, "limit": limit, "last_id": last_id}
        return await self._client.post("/v1/returns/list", json=body)

    async def get_rfbs_returns(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v2/returns/rfbs/list — список rFBS возвратов."""
        body = {"filter": filter or {}, "limit": limit, "offset": offset}
        return await self._client.post("/v2/returns/rfbs/list", json=body)

    async def get_rfbs_return(self, *, return_id: int) -> dict:
        """POST /v2/returns/rfbs/get — детали rFBS возврата."""
        return await self._client.post("/v2/returns/rfbs/get", json={"return_id": return_id})
