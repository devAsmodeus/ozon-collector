from litestar import Router
from src.api.ozon.reports_ext.reports import OzonReportsController
ozon_reports_router = Router(path="/reports", route_handlers=[OzonReportsController])
