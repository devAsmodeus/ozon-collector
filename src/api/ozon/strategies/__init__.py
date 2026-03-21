from litestar import Router
from src.api.ozon.strategies.strategies import OzonStrategiesController
ozon_strategies_router = Router(path="/strategies", route_handlers=[OzonStrategiesController])
