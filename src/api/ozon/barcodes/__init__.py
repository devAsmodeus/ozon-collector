from litestar import Router
from src.api.ozon.barcodes.barcodes import OzonBarcodesController
ozon_barcodes_router = Router(path="/barcodes", route_handlers=[OzonBarcodesController])
