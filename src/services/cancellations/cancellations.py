"""Сервис: Отмены заказов."""
from src.collectors.cancellations.cancellations import CancellationsCollector
from src.services.base import BaseService


class CancellationsService(BaseService):
    async def get_list(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        async with CancellationsCollector() as c:
            return await c.get_list(filter=filter, limit=limit, offset=offset)

    async def approve(self, *, cancellation_id: int) -> dict:
        async with CancellationsCollector() as c:
            return await c.approve(cancellation_id=cancellation_id)

    async def reject(self, *, cancellation_id: int, reason: str = "") -> dict:
        async with CancellationsCollector() as c:
            return await c.reject(cancellation_id=cancellation_id, reason=reason)
