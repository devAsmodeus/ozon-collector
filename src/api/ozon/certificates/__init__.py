from litestar import Router
from src.api.ozon.certificates.certificates import OzonCertificatesController
ozon_certificates_router = Router(path="/certificates", route_handlers=[OzonCertificatesController])
