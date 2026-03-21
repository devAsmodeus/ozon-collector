"""Ozon API proxy: Products / Карточки товаров."""
from litestar import Controller, get, post

from src.services.products.products import ProductsService


class OzonProductsController(Controller):
    path = "/cards"
    tags = ["Products — Карточки"]

    @post(
        "/list",
        summary="Список товаров (Ozon API)",
        description="**Ozon:** `POST /v2/product/list`",
    )
    async def get_product_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ProductsService().get_product_list(
            filter=params.get("filter"),
            last_id=params.get("last_id", ""),
            limit=params.get("limit", 100),
        )

    @post(
        "/info",
        summary="Информация о товаре (Ozon API)",
        description="**Ozon:** `POST /v2/product/info`",
    )
    async def get_product_info(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ProductsService().get_product_info(
            product_id=params.get("product_id", 0),
            offer_id=params.get("offer_id", ""),
            sku=params.get("sku", 0),
        )

    @post(
        "/info/list",
        summary="Информация о нескольких товарах (Ozon API)",
        description="**Ozon:** `POST /v2/product/info/list`",
    )
    async def get_product_info_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ProductsService().get_product_info_list(
            product_id=params.get("product_id"),
            offer_id=params.get("offer_id"),
        )

    @post(
        "/attributes",
        summary="Атрибуты товаров (Ozon API)",
        description="**Ozon:** `POST /v3/products/info/attributes`",
    )
    async def get_product_attributes(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ProductsService().get_product_attributes(
            filter=params.get("filter"),
            limit=params.get("limit", 100),
            last_id=params.get("last_id", ""),
        )
