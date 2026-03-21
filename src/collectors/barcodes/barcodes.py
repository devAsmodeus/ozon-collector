"""Коллектор: Штрихкоды."""
from src.collectors.base import OzonApiClient


class BarcodesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def generate(self, *, count: int = 1) -> dict:
        """POST /v1/barcode/generate — генерация штрихкодов."""
        return await self._client.post("/v1/barcode/generate", json={"count": count})

    async def bind(self, *, barcodes: list[dict]) -> dict:
        """POST /v1/barcode/bind — привязка штрихкодов к товарам."""
        return await self._client.post("/v1/barcode/bind", json={"barcodes": barcodes})
