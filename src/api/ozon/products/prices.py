"""Ozon API proxy: Products / Цены."""
from litestar import Controller, post

from src.services.products.prices import PricesService


class OzonPricesController(Controller):
    path = "/prices"
    tags = ["Products — Цены"]

    @post(
        "/list",
        summary="Цены товаров (Ozon API)",
        description="**Ozon:** `POST /v4/product/info/prices`",
    )
    async def get_prices(self, data: dict | None = None) -> dict:
        params = data or {}
        return await PricesService().get_prices(
            filter=params.get("filter"),
            last_id=params.get("last_id", ""),
            limit=params.get("limit", 100),
        )
