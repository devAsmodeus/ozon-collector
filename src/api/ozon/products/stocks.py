"""Ozon API proxy: Products / Остатки и склады."""
from litestar import Controller, get, post

from src.services.products.stocks import StocksService


class OzonStocksController(Controller):
    path = "/stocks"
    tags = ["Products — Остатки"]

    @post(
        "/list",
        summary="Остатки товаров (Ozon API)",
        description="**Ozon:** `POST /v3/product/info/stocks`",
    )
    async def get_stocks_info(self, data: dict | None = None) -> dict:
        params = data or {}
        return await StocksService().get_stocks_info(
            filter=params.get("filter"),
            last_id=params.get("last_id", ""),
            limit=params.get("limit", 100),
        )

    @get(
        "/warehouses",
        summary="Список складов продавца (Ozon API)",
        description="**Ozon:** `POST /v1/warehouse/list`",
    )
    async def get_warehouse_list(self) -> dict:
        return await StocksService().get_warehouse_list()
