"""Сервис: Общее — Информация о продавце."""
import logging

from src.collectors.general.seller import SellerCollector
from src.schemas.general.seller import SellerInfo
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class SellerService(BaseService):

    async def get_seller_info(self) -> SellerInfo:
        """Получает данные продавца из Ozon API (без сохранения в БД)."""
        async with SellerCollector() as c:
            return await c.get_seller_info()

    async def sync_seller_info(self) -> SellerInfo:
        """Получает и сохраняет данные продавца в БД."""
        async with SellerCollector() as c:
            seller = await c.get_seller_info()
        async with self.db as db:
            result = await db.seller.upsert(seller)
            await db.commit()
        logger.info("Seller info synced: %s (%s)", result.name, result.company_id)
        return result
