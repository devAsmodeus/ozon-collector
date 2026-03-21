from litestar import Router
from src.api.ozon.returns.returns import OzonReturnsController
ozon_returns_router = Router(path="/returns", route_handlers=[OzonReturnsController])
