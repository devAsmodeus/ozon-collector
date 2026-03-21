"""Коллектор: Товары — Цены."""
from src.collectors.base import OzonApiClient


class PricesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_prices(self, *, filter: dict | None = None, last_id: str = "", limit: int = 100) -> dict:
        """POST /v4/product/info/prices — цены товаров."""
        body = {"filter": filter or {"visibility": "ALL"}, "last_id": last_id, "limit": limit}
        return await self._client.post("/v4/product/info/prices", json=body)

    async def update_prices(self, *, prices: list[dict]) -> dict:
        """POST /v1/product/import/prices — обновить цены. ⚠️ Мутация."""
        return await self._client.post("/v1/product/import/prices", json={"prices": prices})
