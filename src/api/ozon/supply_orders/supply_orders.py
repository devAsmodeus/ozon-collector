"""Ozon API proxy: Заявки на поставку FBO."""
from litestar import Controller, post
from src.services.supply_orders.supply_orders import SupplyOrdersService


class OzonSupplyOrdersController(Controller):
    path = "/"
    tags = ["Поставки FBO"]

    @post("/list", summary="Список заявок на поставку (Ozon API)")
    async def list_supply_orders(self, data: dict | None = None) -> dict:
        params = data or {}
        return await SupplyOrdersService().list_supply_orders(filter=params.get("filter"), limit=params.get("limit", 100))

    @post("/get", summary="Детали заявки на поставку (Ozon API)")
    async def get_supply_order(self, data: dict) -> dict:
        return await SupplyOrdersService().get_supply_order(supply_order_id=data["supply_order_id"])
