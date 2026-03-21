from litestar import Router

from src.api.sync.general.seller import SyncSellerController

sync_general_router = Router(
    path="/general",
    route_handlers=[SyncSellerController],
)
