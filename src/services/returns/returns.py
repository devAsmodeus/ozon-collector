"""Сервис: Возвраты."""
from src.collectors.returns.returns import ReturnsCollector
from src.services.base import BaseService


class ReturnsService(BaseService):
    async def get_fbo_returns(self, *, filter: dict | None = None, limit: int = 100, last_id: int = 0) -> dict:
        async with ReturnsCollector() as c:
            return await c.get_fbo_returns(filter=filter, limit=limit, last_id=last_id)

    async def get_rfbs_returns(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        async with ReturnsCollector() as c:
            return await c.get_rfbs_returns(filter=filter, limit=limit, offset=offset)

    async def get_rfbs_return(self, *, return_id: int) -> dict:
        async with ReturnsCollector() as c:
            return await c.get_rfbs_return(return_id=return_id)
