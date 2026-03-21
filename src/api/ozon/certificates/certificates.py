"""Ozon API proxy: Сертификаты."""
from litestar import Controller, post
from src.services.certificates.certificates import CertificatesService


class OzonCertificatesController(Controller):
    path = "/"
    tags = ["Сертификаты"]

    @post("/list", summary="Список сертификатов (Ozon API)")
    async def list_certificates(self, data: dict | None = None) -> dict:
        params = data or {}
        return await CertificatesService().list_certificates(page=params.get("page", 1), page_size=params.get("page_size", 100))

    @post("/info", summary="Информация о сертификате (Ozon API)")
    async def get_certificate_info(self, data: dict) -> dict:
        return await CertificatesService().get_certificate_info(certificate_id=data["certificate_id"])
