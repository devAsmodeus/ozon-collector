"""Сервис: Категории и атрибуты."""
from src.collectors.categories.categories import CategoriesCollector
from src.services.base import BaseService


class CategoriesService(BaseService):
    async def get_category_tree(self, *, language: str = "DEFAULT") -> dict:
        async with CategoriesCollector() as c:
            return await c.get_category_tree(language=language)

    async def get_category_attributes(self, *, description_category_id: int, type_id: int = 0, language: str = "DEFAULT") -> dict:
        async with CategoriesCollector() as c:
            return await c.get_category_attributes(description_category_id=description_category_id, type_id=type_id, language=language)

    async def get_attribute_values(self, *, attribute_id: int, description_category_id: int, type_id: int = 0, limit: int = 100, last_value_id: int = 0) -> dict:
        async with CategoriesCollector() as c:
            return await c.get_attribute_values(attribute_id=attribute_id, description_category_id=description_category_id, type_id=type_id, limit=limit, last_value_id=last_value_id)
