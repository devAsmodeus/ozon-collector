"""Сервис: Сертификаты."""
from src.collectors.certificates.certificates import CertificatesCollector
from src.services.base import BaseService


class CertificatesService(BaseService):
    async def list_certificates(self, *, page: int = 1, page_size: int = 100) -> dict:
        async with CertificatesCollector() as c:
            return await c.list_certificates(page=page, page_size=page_size)

    async def get_certificate_info(self, *, certificate_id: int) -> dict:
        async with CertificatesCollector() as c:
            return await c.get_certificate_info(certificate_id=certificate_id)
