"""Коллектор: Заказы FBS — отправления."""
from src.collectors.base import OzonApiClient


class FbsPostingsCollector:
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
        """POST /v3/posting/fbs/list — список отправлений FBS."""
        body = {
            "dir": dir,
            "filter": filter or {},
            "limit": limit,
            "offset": offset,
        }
        if with_:
            body["with"] = with_
        return await self._client.post("/v3/posting/fbs/list", json=body)

    async def get_posting(self, *, posting_number: str, with_: dict | None = None) -> dict:
        """POST /v3/posting/fbs/get — детали отправления FBS."""
        body = {"posting_number": posting_number}
        if with_:
            body["with"] = with_
        return await self._client.post("/v3/posting/fbs/get", json=body)

    async def get_unfulfilled_list(
        self,
        *,
        dir: str = "ASC",
        filter: dict | None = None,
        limit: int = 50,
        offset: int = 0,
        with_: dict | None = None,
    ) -> dict:
        """POST /v3/posting/fbs/unfulfilled/list — необработанные отправления."""
        body = {"dir": dir, "filter": filter or {}, "limit": limit, "offset": offset}
        if with_:
            body["with"] = with_
        return await self._client.post("/v3/posting/fbs/unfulfilled/list", json=body)
