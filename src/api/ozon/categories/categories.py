"""Ozon API proxy: Категории и атрибуты."""
from litestar import Controller, get, post
from src.services.categories.categories import CategoriesService


class OzonCategoriesController(Controller):
    path = "/"
    tags = ["Категории"]

    @get("/tree", summary="Дерево категорий (Ozon API)")
    async def get_category_tree(self) -> dict:
        return await CategoriesService().get_category_tree()

    @post("/attributes", summary="Атрибуты категории (Ozon API)")
    async def get_category_attributes(self, data: dict) -> dict:
        return await CategoriesService().get_category_attributes(
            description_category_id=data["description_category_id"],
            type_id=data.get("type_id", 0),
        )

    @post("/attribute-values", summary="Значения атрибута (Ozon API)")
    async def get_attribute_values(self, data: dict) -> dict:
        return await CategoriesService().get_attribute_values(
            attribute_id=data["attribute_id"],
            description_category_id=data["description_category_id"],
            type_id=data.get("type_id", 0),
            limit=data.get("limit", 100),
        )
