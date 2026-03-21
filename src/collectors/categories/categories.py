"""Коллектор: Категории и атрибуты."""
from src.collectors.base import OzonApiClient


class CategoriesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_category_tree(self, *, language: str = "DEFAULT") -> dict:
        """POST /v1/description-category/tree — дерево категорий."""
        return await self._client.post("/v1/description-category/tree", json={"language": language})

    async def get_category_attributes(self, *, description_category_id: int, type_id: int = 0, language: str = "DEFAULT") -> dict:
        """POST /v1/description-category/attribute — атрибуты категории."""
        return await self._client.post("/v1/description-category/attribute", json={
            "description_category_id": description_category_id,
            "type_id": type_id,
            "language": language,
        })

    async def get_attribute_values(self, *, attribute_id: int, description_category_id: int, type_id: int = 0, limit: int = 100, last_value_id: int = 0, language: str = "DEFAULT") -> dict:
        """POST /v1/description-category/attribute/values — значения атрибута."""
        return await self._client.post("/v1/description-category/attribute/values", json={
            "attribute_id": attribute_id,
            "description_category_id": description_category_id,
            "type_id": type_id,
            "limit": limit,
            "last_value_id": last_value_id,
            "language": language,
        })
