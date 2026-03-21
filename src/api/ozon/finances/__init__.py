from litestar import Router

from src.api.ozon.finances.finances import OzonFinancesController

ozon_finances_router = Router(
    path="/finances",
    route_handlers=[OzonFinancesController],
)
