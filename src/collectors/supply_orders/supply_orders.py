"""Коллектор: Заявки на поставку FBO."""
from src.collectors.base import OzonApiClient


class SupplyOrdersCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_supply_orders(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v2/supply-order/list — список заявок на поставку."""
        body = {"filter": filter or {}, "limit": limit, "offset": offset}
        return await self._client.post("/v2/supply-order/list", json=body)

    async def get_supply_order(self, *, supply_order_id: int) -> dict:
        """POST /v2/supply-order/get — детали заявки на поставку."""
        return await self._client.post("/v2/supply-order/get", json={"supply_order_id": supply_order_id})
