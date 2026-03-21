from litestar import Router
from src.api.ozon.fbs_actions.actions import OzonFbsActionsController
ozon_fbs_actions_router = Router(path="/fbs-actions", route_handlers=[OzonFbsActionsController])
