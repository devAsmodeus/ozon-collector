"""Ozon API proxy: Штрихкоды."""
from litestar import Controller, post
from src.services.barcodes.barcodes import BarcodesService


class OzonBarcodesController(Controller):
    path = "/"
    tags = ["Штрихкоды"]

    @post("/generate", summary="Генерация штрихкодов (Ozon API)")
    async def generate(self, data: dict | None = None) -> dict:
        params = data or {}
        return await BarcodesService().generate(count=params.get("count", 1))
