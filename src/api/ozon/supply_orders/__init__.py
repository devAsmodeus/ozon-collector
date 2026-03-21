from litestar import Router
from src.api.ozon.supply_orders.supply_orders import OzonSupplyOrdersController
ozon_supply_orders_router = Router(path="/supply-orders", route_handlers=[OzonSupplyOrdersController])
