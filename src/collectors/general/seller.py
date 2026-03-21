"""Коллектор: Общее — Информация о продавце Ozon."""
from src.collectors.base import OzonApiClient
from src.schemas.general.seller import SellerInfo


class SellerCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_seller_info(self) -> SellerInfo:
        """POST /v1/seller/info — информация о продавце."""
        data = await self._client.post("/v1/seller/info")
        return SellerInfo(
            name=data.get("name", ""),
            company_id=str(data.get("company_id", "")),
        )
