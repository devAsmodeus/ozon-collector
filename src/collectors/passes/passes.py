"""Коллектор: Пропуска и полигоны доставки."""
from src.collectors.base import OzonApiClient


class PassesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_passes(self, *, filter: dict | None = None) -> dict:
        """POST /v1/pass/list — список пропусков."""
        return await self._client.post("/v1/pass/list", json={"filter": filter or {}})

    async def create_carriage_pass(self, *, data: dict) -> dict:
        """POST /v1/carriage/pass/create — создать пропуск на поставку. ⚠️ Мутация."""
        return await self._client.post("/v1/carriage/pass/create", json=data)

    async def create_return_pass(self, *, data: dict) -> dict:
        """POST /v1/return/pass/create — создать пропуск на возврат. ⚠️ Мутация."""
        return await self._client.post("/v1/return/pass/create", json=data)

    async def create_polygon(self, *, data: dict) -> dict:
        """POST /v1/polygon/create — создать полигон доставки. ⚠️ Мутация."""
        return await self._client.post("/v1/polygon/create", json=data)

    async def bind_polygon(self, *, delivery_method_id: int, polygon_id: int) -> dict:
        """POST /v1/polygon/bind — привязать способ доставки к полигону. ⚠️ Мутация."""
        return await self._client.post("/v1/polygon/bind", json={
            "delivery_method_id": delivery_method_id, "polygon_id": polygon_id,
        })
