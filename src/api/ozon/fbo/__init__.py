from litestar import Router

from src.api.ozon.fbo.postings import OzonFboPostingsController

ozon_fbo_router = Router(
    path="/fbo",
    route_handlers=[OzonFboPostingsController],
)
