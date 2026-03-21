"""Сервис: Заявки на поставку FBO."""
from src.collectors.supply_orders.supply_orders import SupplyOrdersCollector
from src.services.base import BaseService


class SupplyOrdersService(BaseService):
    async def list_supply_orders(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        async with SupplyOrdersCollector() as c:
            return await c.list_supply_orders(filter=filter, limit=limit, offset=offset)

    async def get_supply_order(self, *, supply_order_id: int) -> dict:
        async with SupplyOrdersCollector() as c:
            return await c.get_supply_order(supply_order_id=supply_order_id)
