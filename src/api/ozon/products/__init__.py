from litestar import Router

from src.api.ozon.products.products import OzonProductsController
from src.api.ozon.products.prices import OzonPricesController
from src.api.ozon.products.stocks import OzonStocksController

ozon_products_router = Router(
    path="/products",
    route_handlers=[OzonProductsController, OzonPricesController, OzonStocksController],
)
