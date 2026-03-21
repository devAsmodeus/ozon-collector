"""Коллектор: Акции и промо."""
from src.collectors.base import OzonApiClient


class PromotionsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_promotions_list(self) -> dict:
        """POST /v1/actions — список акций."""
        return await self._client.post("/v1/actions")

    async def get_promotion_products(self, *, action_id: int, limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/actions/products — товары в акции."""
        body = {"action_id": action_id, "limit": limit, "offset": offset}
        return await self._client.post("/v1/actions/products", json=body)

    async def get_hot_sales_list(self) -> dict:
        """POST /v1/actions/hotsales/list — список распродаж."""
        return await self._client.post("/v1/actions/hotsales/list")
