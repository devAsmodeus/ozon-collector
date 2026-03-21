"""Сервис: Товары — Цены."""
import logging

from src.collectors.products.prices import PricesCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class PricesService(BaseService):

    async def get_prices(self, *, filter: dict | None = None, last_id: str = "", limit: int = 100) -> dict:
        async with PricesCollector() as c:
            return await c.get_prices(filter=filter, last_id=last_id, limit=limit)
