"""Ozon API proxy: Возвраты."""
from litestar import Controller, post
from src.services.returns.returns import ReturnsService


class OzonReturnsController(Controller):
    path = "/"
    tags = ["Возвраты"]

    @post("/fbo/list", summary="FBO возвраты (Ozon API)")
    async def get_fbo_returns(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ReturnsService().get_fbo_returns(filter=params.get("filter"), limit=params.get("limit", 100))

    @post("/rfbs/list", summary="rFBS возвраты (Ozon API)")
    async def get_rfbs_returns(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ReturnsService().get_rfbs_returns(filter=params.get("filter"), limit=params.get("limit", 100))

    @post("/rfbs/get", summary="Детали rFBS возврата (Ozon API)")
    async def get_rfbs_return(self, data: dict) -> dict:
        return await ReturnsService().get_rfbs_return(return_id=data["return_id"])
