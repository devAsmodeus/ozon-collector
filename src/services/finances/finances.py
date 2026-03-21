"""Сервис: Финансы — транзакции."""
import logging

from src.collectors.finances.finances import FinancesCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class FinancesService(BaseService):

    async def get_transaction_list(self, *, filter: dict | None = None, page: int = 1, page_size: int = 100) -> dict:
        async with FinancesCollector() as c:
            return await c.get_transaction_list(filter=filter, page=page, page_size=page_size)

    async def get_totals(self) -> dict:
        async with FinancesCollector() as c:
            return await c.get_totals()
