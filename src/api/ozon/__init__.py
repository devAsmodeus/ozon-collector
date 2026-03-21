"""Ozon API proxy router — /ozon/*"""
from litestar import Router

from src.api.ozon.general import ozon_general_router
from src.api.ozon.products import ozon_products_router
from src.api.ozon.fbs import ozon_fbs_router
from src.api.ozon.fbo import ozon_fbo_router
from src.api.ozon.analytics import ozon_analytics_router
from src.api.ozon.finances import ozon_finances_router
from src.api.ozon.promotions import ozon_promotions_router

ozon_router = Router(
    path="/ozon",
    route_handlers=[
        ozon_general_router,
        ozon_products_router,
        ozon_fbs_router,
        ozon_fbo_router,
        ozon_analytics_router,
        ozon_finances_router,
        ozon_promotions_router,
    ],
)
