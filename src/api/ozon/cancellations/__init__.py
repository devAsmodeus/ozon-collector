from litestar import Router
from src.api.ozon.cancellations.cancellations import OzonCancellationsController
ozon_cancellations_router = Router(path="/cancellations", route_handlers=[OzonCancellationsController])
