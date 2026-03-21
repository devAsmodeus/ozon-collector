"""Ozon API proxy: FBS действия."""
from litestar import Controller, post
from src.services.fbs_actions.actions import FbsActionsService


class OzonFbsActionsController(Controller):
    path = "/"
    tags = ["FBS Действия"]

    @post("/ship", summary="Отгрузить отправление FBS (Ozon API)")
    async def ship_posting(self, data: dict) -> dict:
        return await FbsActionsService().ship_posting(posting_number=data["posting_number"], packages=data["packages"])

    @post("/act/create", summary="Создать акт (Ozon API)")
    async def create_act(self, data: dict) -> dict:
        return await FbsActionsService().create_act(delivery_method_id=data["delivery_method_id"], departure_date=data["departure_date"])

    @post("/act/status", summary="Статус акта (Ozon API)")
    async def check_act_status(self, data: dict) -> dict:
        return await FbsActionsService().check_act_status(id=data["id"])

    @post("/labels", summary="Этикетки отправлений (Ozon API)")
    async def get_package_label(self, data: dict) -> dict:
        return await FbsActionsService().get_package_label(posting_number=data["posting_number"])

    @post("/set-delivering", summary="Статус 'доставляется' (Ozon API)")
    async def set_delivering(self, data: dict) -> dict:
        return await FbsActionsService().set_delivering(posting_number=data["posting_number"])
