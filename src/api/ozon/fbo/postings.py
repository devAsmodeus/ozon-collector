"""Ozon API proxy: FBO / Отправления."""
from litestar import Controller, post

from src.services.fbo.postings import FboPostingsService


class OzonFboPostingsController(Controller):
    path = "/postings"
    tags = ["Отправления FBO"]

    @post(
        "/list",
        summary="Список отправлений FBO (Ozon API)",
        description="**Ozon:** `POST /v2/posting/fbo/list`",
    )
    async def get_posting_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await FboPostingsService().get_posting_list(
            dir=params.get("dir", "ASC"),
            filter=params.get("filter"),
            limit=params.get("limit", 50),
            offset=params.get("offset", 0),
            with_=params.get("with"),
        )

    @post(
        "/get",
        summary="Детали отправления FBO (Ozon API)",
        description="**Ozon:** `POST /v2/posting/fbo/get`",
    )
    async def get_posting(self, data: dict) -> dict:
        return await FboPostingsService().get_posting(
            posting_number=data["posting_number"],
            with_=data.get("with"),
        )
