"""Ozon API proxy: Ценовые стратегии."""
from litestar import Controller, get, post
from src.services.strategies.strategies import StrategiesService


class OzonStrategiesController(Controller):
    path = "/"
    tags = ["Ценовые стратегии"]

    @get("/list", summary="Список стратегий (Ozon API)")
    async def list_strategies(self) -> dict:
        return await StrategiesService().list_strategies()

    @post("/info", summary="Детали стратегии (Ozon API)")
    async def get_strategy_info(self, data: dict) -> dict:
        return await StrategiesService().get_strategy_info(strategy_id=data["strategy_id"])
