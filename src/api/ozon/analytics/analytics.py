"""Ozon API proxy: Аналитика."""
from litestar import Controller, post

from src.services.analytics.analytics import AnalyticsService


class OzonAnalyticsController(Controller):
    path = "/"
    tags = ["Аналитика"]

    @post(
        "/data",
        summary="Аналитические данные (Ozon API)",
        description="**Ozon:** `POST /v1/analytics/data`",
    )
    async def get_analytics_data(self, data: dict) -> dict:
        return await AnalyticsService().get_analytics_data(
            date_from=data["date_from"],
            date_to=data["date_to"],
            metrics=data.get("metrics"),
            dimension=data.get("dimension"),
            limit=data.get("limit", 1000),
            offset=data.get("offset", 0),
        )

    @post(
        "/stock-on-warehouses",
        summary="Остатки на складах (Ozon API)",
        description="**Ozon:** `POST /v2/analytics/stock_on_warehouses`",
    )
    async def get_stock_on_warehouses(self, data: dict | None = None) -> dict:
        params = data or {}
        return await AnalyticsService().get_stock_on_warehouses(
            limit=params.get("limit", 100),
            offset=params.get("offset", 0),
        )
