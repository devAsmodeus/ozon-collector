from litestar import Router

from src.api.ozon.general.seller import OzonSellerController

ozon_general_router = Router(
    path="/general",
    route_handlers=[OzonSellerController],
)
