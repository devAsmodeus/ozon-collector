"""Коллектор: Товары — импорт, обновление, архив, удаление."""
from src.collectors.base import OzonApiClient


class ProductImportCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def import_products(self, *, items: list[dict]) -> dict:
        """POST /v3/product/import — создать/обновить товары (до 100). ⚠️ Мутация."""
        return await self._client.post("/v3/product/import", json={"items": items})

    async def get_import_info(self, *, task_id: int) -> dict:
        """POST /v1/product/import/info — статус задачи импорта."""
        return await self._client.post("/v1/product/import/info", json={"task_id": task_id})

    async def import_by_sku(self, *, items: list[dict]) -> dict:
        """POST /v1/product/import-by-sku — копия товара по SKU. ⚠️ Мутация."""
        return await self._client.post("/v1/product/import-by-sku", json={"items": items})

    async def update_attributes(self, *, items: list[dict]) -> dict:
        """POST /v1/product/attributes/update — обновить характеристики. ⚠️ Мутация."""
        return await self._client.post("/v1/product/attributes/update", json={"items": items})

    async def import_pictures(self, *, images: list[dict]) -> dict:
        """POST /v1/product/pictures/import — загрузить изображения. ⚠️ Мутация."""
        return await self._client.post("/v1/product/pictures/import", json={"images": images})

    async def get_pictures_info(self, *, product_id: list[int]) -> dict:
        """POST /v2/product/pictures/info — статус загрузки изображений."""
        return await self._client.post("/v2/product/pictures/info", json={"product_id": product_id})

    async def get_product_description(self, *, offer_id: str = "", product_id: int = 0) -> dict:
        """POST /v1/product/info/description — описание товара."""
        return await self._client.post("/v1/product/info/description", json={
            "offer_id": offer_id, "product_id": product_id,
        })

    async def archive_product(self, *, product_id: list[int]) -> dict:
        """POST /v1/product/archive — перенести в архив. ⚠️ Мутация."""
        return await self._client.post("/v1/product/archive", json={"product_id": product_id})

    async def unarchive_product(self, *, product_id: list[int]) -> dict:
        """POST /v1/product/unarchive — восстановить из архива. ⚠️ Мутация."""
        return await self._client.post("/v1/product/unarchive", json={"product_id": product_id})

    async def delete_products(self, *, product_id: list[int]) -> dict:
        """POST /v2/products/delete — удалить товары без SKU. ⚠️ Мутация."""
        return await self._client.post("/v2/products/delete", json={"product_id": product_id})

    async def get_product_limit(self) -> dict:
        """POST /v4/product/info/limit — лимиты создания товаров."""
        return await self._client.post("/v4/product/info/limit")

    async def get_rating_by_sku(self, *, skus: list[int]) -> dict:
        """POST /v1/product/rating-by-sku — рейтинг контента товара."""
        return await self._client.post("/v1/product/rating-by-sku", json={"skus": skus})

    async def update_offer_id(self, *, update_offer_id: list[dict]) -> dict:
        """POST /v1/product/update/offer-id — обновить offer_id. ⚠️ Мутация."""
        return await self._client.post("/v1/product/update/offer-id", json={"update_offer_id": update_offer_id})

    async def get_related_skus(self, *, sku: list[int]) -> dict:
        """POST /v1/product/related-sku/get — единый SKU по старым FBO/FBS."""
        return await self._client.post("/v1/product/related-sku/get", json={"sku": sku})

    async def get_subscription_count(self, *, skus: list[int]) -> dict:
        """POST /v1/product/info/subscription — подписки на товар."""
        return await self._client.post("/v1/product/info/subscription", json={"skus": skus})
