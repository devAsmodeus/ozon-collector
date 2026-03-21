"""Ozon API proxy: General / Продавец."""
from litestar import Controller, get

from src.schemas.general.seller import SellerInfo
from src.services.general.seller import SellerService


class OzonSellerController(Controller):
    path = "/seller"
    tags = ["Ozon / General"]

    @get(
        "/info",
        summary="Информация о продавце (Ozon API)",
        description="**Ozon:** `POST api-seller.ozon.ru/v1/seller/info`",
    )
    async def get_seller_info(self) -> SellerInfo:
        return await SellerService().get_seller_info()
