"""Сервис: Акции и промо."""
import logging

from src.collectors.promotions.promotions import PromotionsCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class PromotionsService(BaseService):

    async def get_promotions_list(self) -> dict:
        async with PromotionsCollector() as c:
            return await c.get_promotions_list()

    async def get_promotion_products(self, *, action_id: int, limit: int = 100, offset: int = 0) -> dict:
        async with PromotionsCollector() as c:
            return await c.get_promotion_products(action_id=action_id, limit=limit, offset=offset)

    async def get_hot_sales_list(self) -> dict:
        async with PromotionsCollector() as c:
            return await c.get_hot_sales_list()
