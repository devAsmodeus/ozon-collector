"""Ozon API proxy: FBS / Отправления."""
from litestar import Controller, post

from src.services.fbs.postings import FbsPostingsService


class OzonFbsPostingsController(Controller):
    path = "/postings"
    tags = ["Отправления FBS"]

    @post(
        "/list",
        summary="Список отправлений FBS (Ozon API)",
        description="**Ozon:** `POST /v3/posting/fbs/list`",
    )
    async def get_posting_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await FbsPostingsService().get_posting_list(
            dir=params.get("dir", "ASC"),
            filter=params.get("filter"),
            limit=params.get("limit", 50),
            offset=params.get("offset", 0),
            with_=params.get("with"),
        )

    @post(
        "/get",
        summary="Детали отправления FBS (Ozon API)",
        description="**Ozon:** `POST /v3/posting/fbs/get`",
    )
    async def get_posting(self, data: dict) -> dict:
        return await FbsPostingsService().get_posting(
            posting_number=data["posting_number"],
            with_=data.get("with"),
        )

    @post(
        "/unfulfilled",
        summary="Необработанные отправления FBS (Ozon API)",
        description="**Ozon:** `POST /v3/posting/fbs/unfulfilled/list`",
    )
    async def get_unfulfilled_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await FbsPostingsService().get_unfulfilled_list(
            dir=params.get("dir", "ASC"),
            filter=params.get("filter"),
            limit=params.get("limit", 50),
            offset=params.get("offset", 0),
            with_=params.get("with"),
        )
