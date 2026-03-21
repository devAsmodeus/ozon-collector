"""Ozon API proxy: Акции и промо."""
from litestar import Controller, get, post

from src.services.promotions.promotions import PromotionsService


class OzonPromotionsController(Controller):
    path = "/"
    tags = ["Акции"]

    @get(
        "/list",
        summary="Список акций (Ozon API)",
        description="**Ozon:** `POST /v1/actions`",
    )
    async def get_promotions_list(self) -> dict:
        return await PromotionsService().get_promotions_list()

    @post(
        "/products",
        summary="Товары в акции (Ozon API)",
        description="**Ozon:** `POST /v1/actions/products`",
    )
    async def get_promotion_products(self, data: dict) -> dict:
        return await PromotionsService().get_promotion_products(
            action_id=data["action_id"],
            limit=data.get("limit", 100),
            offset=data.get("offset", 0),
        )

    @get(
        "/hotsales",
        summary="Распродажи (Ozon API)",
        description="**Ozon:** `POST /v1/actions/hotsales/list`",
    )
    async def get_hot_sales_list(self) -> dict:
        return await PromotionsService().get_hot_sales_list()
