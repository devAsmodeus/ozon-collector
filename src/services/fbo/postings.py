"""Сервис: Заказы FBO — отправления."""
import logging

from src.collectors.fbo.postings import FboPostingsCollector
from src.services.base import BaseService

logger = logging.getLogger(__name__)


class FboPostingsService(BaseService):

    async def get_posting_list(self, *, dir: str = "ASC", filter: dict | None = None, limit: int = 50, offset: int = 0, with_: dict | None = None) -> dict:
        async with FboPostingsCollector() as c:
            return await c.get_posting_list(dir=dir, filter=filter, limit=limit, offset=offset, with_=with_)

    async def get_posting(self, *, posting_number: str, with_: dict | None = None) -> dict:
        async with FboPostingsCollector() as c:
            return await c.get_posting(posting_number=posting_number, with_=with_)
