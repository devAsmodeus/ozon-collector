"""Сервис: Аналитика продавца."""
import logging

from src.collectors.analytics.analytics import AnalyticsCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class AnalyticsService(BaseService):

    async def get_analytics_data(self, *, date_from: str, date_to: str, metrics: list[str] | None = None, dimension: list[str] | None = None, limit: int = 1000, offset: int = 0) -> dict:
        async with AnalyticsCollector() as c:
            return await c.get_analytics_data(
                date_from=date_from, date_to=date_to,
                metrics=metrics, dimension=dimension,
                limit=limit, offset=offset,
            )

    async def get_stock_on_warehouses(self, *, limit: int = 100, offset: int = 0) -> dict:
        async with AnalyticsCollector() as c:
            return await c.get_stock_on_warehouses(limit=limit, offset=offset)
