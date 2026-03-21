"""Коллектор: Заказы FBO — отправления."""
from src.collectors.base import OzonApiClient


class FboPostingsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_posting_list(
        self,
        *,
        dir: str = "ASC",
        filter: dict | None = None,
        limit: int = 50,
        offset: int = 0,
        with_: dict | None = None,
    ) -> dict:
        """POST /v2/posting/fbo/list — список отправлений FBO."""
        body = {
            "dir": dir,
            "filter": filter or {},
            "limit": limit,
            "offset": offset,
        }
        if with_:
            body["with"] = with_
        return await self._client.post("/v2/posting/fbo/list", json=body)

    async def get_posting(self, *, posting_number: str, with_: dict | None = None) -> dict:
        """POST /v2/posting/fbo/get — детали отправления FBO."""
        body = {"posting_number": posting_number}
        if with_:
            body["with"] = with_
        return await self._client.post("/v2/posting/fbo/get", json=body)
