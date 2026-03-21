from litestar import Router
from src.api.ozon.categories.categories import OzonCategoriesController
ozon_categories_router = Router(path="/categories", route_handlers=[OzonCategoriesController])
