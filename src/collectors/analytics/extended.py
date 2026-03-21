"""Коллектор: Аналитика — расширенные методы."""
from src.collectors.base import OzonApiClient


class AnalyticsExtendedCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_product_queries(self, *, date_from: str, date_to: str, limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/analytics/product-queries — поисковые запросы по товарам."""
        return await self._client.post("/v1/analytics/product-queries", json={
            "date_from": date_from, "date_to": date_to, "limit": limit, "offset": offset,
        })

    async def get_turnover_stocks(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/analytics/turnover/stocks — оборачиваемость остатков."""
        return await self._client.post("/v1/analytics/turnover/stocks", json={
            "filter": filter or {}, "limit": limit, "offset": offset,
        })

    async def get_manage_stocks(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/analytics/manage/stocks — управление остатками FBO."""
        return await self._client.post("/v1/analytics/manage/stocks", json={
            "filter": filter or {}, "limit": limit, "offset": offset,
        })

    async def get_stocks(self, *, limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/analytics/stocks — баланс остатков."""
        return await self._client.post("/v1/analytics/stocks", json={"limit": limit, "offset": offset})

    async def get_average_delivery_time(self) -> dict:
        """POST /v1/analytics/average-delivery-time — среднее время доставки."""
        return await self._client.post("/v1/analytics/average-delivery-time")
