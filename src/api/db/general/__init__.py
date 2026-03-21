from litestar import Router

from src.api.db.general.seller import DbSellerController

db_general_router = Router(
    path="/general",
    route_handlers=[DbSellerController],
)
