"""Сервис: Штрихкоды."""
from src.collectors.barcodes.barcodes import BarcodesCollector
from src.services.base import BaseService


class BarcodesService(BaseService):
    async def generate(self, *, count: int = 1) -> dict:
        async with BarcodesCollector() as c:
            return await c.generate(count=count)
