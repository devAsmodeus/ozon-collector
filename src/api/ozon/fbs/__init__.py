from litestar import Router

from src.api.ozon.fbs.postings import OzonFbsPostingsController

ozon_fbs_router = Router(
    path="/fbs",
    route_handlers=[OzonFbsPostingsController],
)
