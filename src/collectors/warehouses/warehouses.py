"""Коллектор: Склады — расширенное управление."""
from src.collectors.base import OzonApiClient


class WarehousesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_warehouses(self) -> dict:
        """POST /v1/warehouse/list — список FBS/rFBS складов."""
        return await self._client.post("/v1/warehouse/list")

    async def list_warehouses_v2(self) -> dict:
        """POST /v2/warehouse/list — детали складов по ID."""
        return await self._client.post("/v2/warehouse/list")

    async def list_delivery_methods(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/delivery-method/list — способы доставки для склада."""
        return await self._client.post("/v1/delivery-method/list", json={
            "filter": filter or {}, "limit": limit, "offset": offset,
        })

    async def create_warehouse(self, *, data: dict) -> dict:
        """POST /v1/warehouse/fbs/create — создать склад. ⚠️ Мутация."""
        return await self._client.post("/v1/warehouse/fbs/create", json=data)

    async def update_warehouse(self, *, data: dict) -> dict:
        """POST /v1/warehouse/fbs/update — обновить склад. ⚠️ Мутация."""
        return await self._client.post("/v1/warehouse/fbs/update", json=data)

    async def archive_warehouse(self, *, warehouse_id: int) -> dict:
        """POST /v1/warehouse/archive — архивировать склад. ⚠️ Мутация."""
        return await self._client.post("/v1/warehouse/archive", json={"warehouse_id": warehouse_id})

    async def unarchive_warehouse(self, *, warehouse_id: int) -> dict:
        """POST /v1/warehouse/unarchive — восстановить склад. ⚠️ Мутация."""
        return await self._client.post("/v1/warehouse/unarchive", json={"warehouse_id": warehouse_id})

    async def get_dropoff_list(self) -> dict:
        """POST /v1/warehouse/fbs/create/drop-off/list — точки приёма."""
        return await self._client.post("/v1/warehouse/fbs/create/drop-off/list")

    async def get_cluster_list(self) -> dict:
        """GET /v1/cluster/list — кластеры и склады Ozon."""
        return await self._client.get("/v1/cluster/list")
