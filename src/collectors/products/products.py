"""Коллектор: Товары — список и информация о товарах."""
from src.collectors.base import OzonApiClient


class ProductsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_product_list(
        self,
        *,
        filter: dict | None = None,
        last_id: str = "",
        limit: int = 100,
    ) -> dict:
        """POST /v2/product/list — список товаров."""
        body = {"filter": filter or {"visibility": "ALL"}, "last_id": last_id, "limit": limit}
        return await self._client.post("/v2/product/list", json=body)

    async def get_product_info(self, *, product_id: int = 0, offer_id: str = "", sku: int = 0) -> dict:
        """POST /v2/product/info — информация о товаре."""
        body = {"product_id": product_id, "offer_id": offer_id, "sku": sku}
        return await self._client.post("/v2/product/info", json=body)

    async def get_product_info_list(self, *, product_id: list[int] | None = None, offer_id: list[str] | None = None) -> dict:
        """POST /v2/product/info/list — информация о нескольких товарах."""
        body = {}
        if product_id:
            body["product_id"] = product_id
        if offer_id:
            body["offer_id"] = offer_id
        return await self._client.post("/v2/product/info/list", json=body)

    async def get_product_attributes(self, *, filter: dict | None = None, limit: int = 100, last_id: str = "") -> dict:
        """POST /v3/products/info/attributes — атрибуты товаров."""
        body = {"filter": filter or {"visibility": "ALL"}, "limit": limit, "last_id": last_id}
        return await self._client.post("/v3/products/info/attributes", json=body)
