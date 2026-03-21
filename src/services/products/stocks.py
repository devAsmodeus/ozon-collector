"""Сервис: Товары — Остатки и склады."""
import logging

from src.collectors.products.stocks import StocksCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class StocksService(BaseService):

    async def get_stocks_info(self, *, filter: dict | None = None, last_id: str = "", limit: int = 100) -> dict:
        async with StocksCollector() as c:
            return await c.get_stocks_info(filter=filter, last_id=last_id, limit=limit)

    async def get_warehouse_list(self) -> dict:
        async with StocksCollector() as c:
            return await c.get_warehouse_list()
