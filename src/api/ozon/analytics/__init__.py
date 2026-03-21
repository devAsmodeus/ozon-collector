from litestar import Router

from src.api.ozon.analytics.analytics import OzonAnalyticsController

ozon_analytics_router = Router(
    path="/analytics",
    route_handlers=[OzonAnalyticsController],
)
