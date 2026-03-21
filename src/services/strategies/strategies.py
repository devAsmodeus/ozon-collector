"""Сервис: Ценовые стратегии."""
from src.collectors.strategies.strategies import StrategiesCollector
from src.services.base import BaseService


class StrategiesService(BaseService):
    async def list_strategies(self) -> dict:
        async with StrategiesCollector() as c:
            return await c.list_strategies()

    async def get_strategy_info(self, *, strategy_id: int) -> dict:
        async with StrategiesCollector() as c:
            return await c.get_strategy_info(strategy_id=strategy_id)
