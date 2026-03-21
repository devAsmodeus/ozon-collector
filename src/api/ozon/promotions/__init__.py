from litestar import Router

from src.api.ozon.promotions.promotions import OzonPromotionsController

ozon_promotions_router = Router(
    path="/promotions",
    route_handlers=[OzonPromotionsController],
)
