"""Ozon API proxy: Отмены."""
from litestar import Controller, post
from src.services.cancellations.cancellations import CancellationsService


class OzonCancellationsController(Controller):
    path = "/"
    tags = ["Отмены"]

    @post("/list", summary="Список отмен (Ozon API)")
    async def get_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await CancellationsService().get_list(filter=params.get("filter"), limit=params.get("limit", 100))

    @post("/approve", summary="Подтвердить отмену (Ozon API)")
    async def approve(self, data: dict) -> dict:
        return await CancellationsService().approve(cancellation_id=data["cancellation_id"])

    @post("/reject", summary="Отклонить отмену (Ozon API)")
    async def reject(self, data: dict) -> dict:
        return await CancellationsService().reject(cancellation_id=data["cancellation_id"], reason=data.get("reason", ""))
