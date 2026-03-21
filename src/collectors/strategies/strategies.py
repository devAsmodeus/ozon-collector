"""Коллектор: Ценовые стратегии."""
from src.collectors.base import OzonApiClient


class StrategiesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_strategies(self) -> dict:
        """POST /v1/pricing-strategy/list — список ценовых стратегий."""
        return await self._client.post("/v1/pricing-strategy/list")

    async def get_strategy_info(self, *, strategy_id: int) -> dict:
        """POST /v1/pricing-strategy/info — детали стратегии."""
        return await self._client.post("/v1/pricing-strategy/info", json={"strategy_id": strategy_id})

    async def create_strategy(self, *, data: dict) -> dict:
        """POST /v1/pricing-strategy/create — создать стратегию. ⚠️ Мутация."""
        return await self._client.post("/v1/pricing-strategy/create", json=data)

    async def change_status(self, *, strategy_id: int, enabled: bool) -> dict:
        """POST /v1/pricing-strategy/change-status — вкл/выкл стратегию. ⚠️ Мутация."""
        return await self._client.post("/v1/pricing-strategy/change-status", json={
            "strategy_id": strategy_id, "enabled": enabled,
        })

    async def add_products(self, *, strategy_id: int, product_id: list[int]) -> dict:
        """POST /v1/pricing-strategy/products/add — добавить товары. ⚠️ Мутация."""
        return await self._client.post("/v1/pricing-strategy/products/add", json={
            "strategy_id": strategy_id, "product_id": product_id,
        })
