"""Коллектор: Аналитика продавца."""
from src.collectors.base import OzonApiClient


class AnalyticsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_analytics_data(
        self,
        *,
        date_from: str,
        date_to: str,
        metrics: list[str] | None = None,
        dimension: list[str] | None = None,
        filters: list[dict] | None = None,
        sort: list[dict] | None = None,
        limit: int = 1000,
        offset: int = 0,
    ) -> dict:
        """POST /v1/analytics/data — аналитические данные."""
        body = {
            "date_from": date_from,
            "date_to": date_to,
            "metrics": metrics or ["revenue", "ordered_units"],
            "dimension": dimension or ["sku"],
            "limit": limit,
            "offset": offset,
        }
        if filters:
            body["filters"] = filters
        if sort:
            body["sort"] = sort
        return await self._client.post("/v1/analytics/data", json=body)

    async def get_stock_on_warehouses(self, *, limit: int = 100, offset: int = 0) -> dict:
        """POST /v2/analytics/stock_on_warehouses — остатки на складах."""
        body = {"limit": limit, "offset": offset}
        return await self._client.post("/v2/analytics/stock_on_warehouses", json=body)
