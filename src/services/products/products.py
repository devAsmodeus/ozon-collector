"""Сервис: Товары — список и информация."""
import logging

from src.collectors.products.products import ProductsCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class ProductsService(BaseService):

    async def get_product_list(self, *, filter: dict | None = None, last_id: str = "", limit: int = 100) -> dict:
        async with ProductsCollector() as c:
            return await c.get_product_list(filter=filter, last_id=last_id, limit=limit)

    async def get_product_info(self, *, product_id: int = 0, offer_id: str = "", sku: int = 0) -> dict:
        async with ProductsCollector() as c:
            return await c.get_product_info(product_id=product_id, offer_id=offer_id, sku=sku)

    async def get_product_info_list(self, *, product_id: list[int] | None = None, offer_id: list[str] | None = None) -> dict:
        async with ProductsCollector() as c:
            return await c.get_product_info_list(product_id=product_id, offer_id=offer_id)

    async def get_product_attributes(self, *, filter: dict | None = None, limit: int = 100, last_id: str = "") -> dict:
        async with ProductsCollector() as c:
            return await c.get_product_attributes(filter=filter, limit=limit, last_id=last_id)
