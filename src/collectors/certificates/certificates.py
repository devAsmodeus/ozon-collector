"""Коллектор: Сертификаты качества и брендов."""
from src.collectors.base import OzonApiClient


class CertificatesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_certificates(self, *, page: int = 1, page_size: int = 100) -> dict:
        """POST /v1/product/certificate/list — список сертификатов."""
        return await self._client.post("/v1/product/certificate/list", json={"page": page, "page_size": page_size})

    async def get_certificate_info(self, *, certificate_id: int) -> dict:
        """POST /v1/product/certificate/info — информация о сертификате."""
        return await self._client.post("/v1/product/certificate/info", json={"certificate_id": certificate_id})

    async def link_to_product(self, *, certificate_id: int, product_id: list[int]) -> dict:
        """POST /v1/product/certificate/bind — привязать к товарам."""
        return await self._client.post("/v1/product/certificate/bind", json={
            "certificate_id": certificate_id, "product_id": product_id,
        })

    async def unlink_from_product(self, *, certificate_id: int, product_id: list[int]) -> dict:
        """POST /v1/product/certificate/unbind — отвязать от товаров."""
        return await self._client.post("/v1/product/certificate/unbind", json={
            "certificate_id": certificate_id, "product_id": product_id,
        })

    async def delete_certificate(self, *, certificate_id: int) -> dict:
        """POST /v1/product/certificate/delete — удалить сертификат."""
        return await self._client.post("/v1/product/certificate/delete", json={"certificate_id": certificate_id})
