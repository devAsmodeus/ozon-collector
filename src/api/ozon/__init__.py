"""Ozon API proxy router — /ozon/*"""
from litestar import Router

from src.api.ozon.general import ozon_general_router
from src.api.ozon.products import ozon_products_router
from src.api.ozon.fbs import ozon_fbs_router
from src.api.ozon.fbo import ozon_fbo_router
from src.api.ozon.analytics import ozon_analytics_router
from src.api.ozon.finances import ozon_finances_router
from src.api.ozon.promotions import ozon_promotions_router
from src.api.ozon.categories import ozon_categories_router
from src.api.ozon.certificates import ozon_certificates_router
from src.api.ozon.barcodes import ozon_barcodes_router
from src.api.ozon.returns import ozon_returns_router
from src.api.ozon.cancellations import ozon_cancellations_router
from src.api.ozon.reviews import ozon_reviews_router
from src.api.ozon.chats import ozon_chats_router
from src.api.ozon.strategies import ozon_strategies_router
from src.api.ozon.fbs_actions import ozon_fbs_actions_router
from src.api.ozon.supply_orders import ozon_supply_orders_router
from src.api.ozon.reports_ext import ozon_reports_router
from src.api.ozon.performance import ozon_performance_router

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
        ozon_categories_router,
        ozon_certificates_router,
        ozon_barcodes_router,
        ozon_returns_router,
        ozon_cancellations_router,
        ozon_reviews_router,
        ozon_chats_router,
        ozon_strategies_router,
        ozon_fbs_actions_router,
        ozon_supply_orders_router,
        ozon_reports_router,
        ozon_performance_router,
    ],
)
