"""Коллектор: Товары — Остатки и склады."""
from src.collectors.base import OzonApiClient


class StocksCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_stocks_info(self, *, filter: dict | None = None, last_id: str = "", limit: int = 100) -> dict:
        """POST /v3/product/info/stocks — остатки товаров."""
        body = {"filter": filter or {"visibility": "ALL"}, "last_id": last_id, "limit": limit}
        return await self._client.post("/v3/product/info/stocks", json=body)

    async def get_warehouse_list(self) -> dict:
        """POST /v1/warehouse/list — список складов продавца."""
        return await self._client.post("/v1/warehouse/list")

    async def update_stocks(self, *, stocks: list[dict]) -> dict:
        """POST /v2/products/stocks — обновить остатки. ⚠️ Мутация."""
        return await self._client.post("/v2/products/stocks", json={"stocks": stocks})
