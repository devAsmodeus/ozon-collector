from litestar import Router
from src.api.ozon.performance.campaigns import OzonPerformanceController
ozon_performance_router = Router(path="/performance", route_handlers=[OzonPerformanceController])
