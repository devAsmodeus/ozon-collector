"""Коллектор: Performance API — рекламные кампании."""
from src.collectors.performance.base import OzonPerformanceClient


class CampaignsCollector:
    def __init__(self):
        self._client = OzonPerformanceClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_campaigns(self) -> dict:
        """GET /api/client/campaign — список рекламных кампаний."""
        return await self._client.get("/api/client/campaign")

    async def get_campaign(self, *, campaign_id: int) -> dict:
        """GET /api/client/campaign/{id} — детали кампании."""
        return await self._client.get(f"/api/client/campaign/{campaign_id}")

    async def get_campaign_products(self, *, campaign_id: int) -> dict:
        """GET /api/client/campaign/{id}/products — товары в кампании."""
        return await self._client.get(f"/api/client/campaign/{campaign_id}/products")

    async def add_products(self, *, campaign_id: int, products: list[dict]) -> dict:
        """POST /api/client/campaign/{id}/products — добавить товары. ⚠️ Мутация."""
        return await self._client.post(f"/api/client/campaign/{campaign_id}/products", json={"products": products})

    async def update_bids(self, *, campaign_id: int, bids: list[dict]) -> dict:
        """PUT /api/client/campaign/{id}/products — обновить ставки. ⚠️ Мутация."""
        return await self._client.put(f"/api/client/campaign/{campaign_id}/products", json={"bids": bids})

    async def update_daily_budget(self, *, campaign_id: int, daily_budget: float) -> dict:
        """PUT /api/client/campaign/{id}/daily_budget — обновить дневной бюджет. ⚠️ Мутация."""
        return await self._client.put(f"/api/client/campaign/{campaign_id}/daily_budget", json={"daily_budget": daily_budget})

    async def create_statistics_report(self, *, campaigns: list[int], date_from: str, date_to: str, group_by: str = "DATE") -> dict:
        """POST /api/client/statistics — запросить отчёт по статистике."""
        return await self._client.post("/api/client/statistics", json={
            "campaigns": campaigns, "dateFrom": date_from, "dateTo": date_to, "groupBy": group_by,
        })

    async def get_statistics_report(self, *, uuid: str) -> dict:
        """GET /api/client/statistics/{uuid} — получить отчёт по UUID."""
        return await self._client.get(f"/api/client/statistics/{uuid}")

    async def get_phrase_statistics(self, *, campaigns: list[int], date_from: str, date_to: str) -> dict:
        """POST /api/client/statistics/phrases — статистика по фразам."""
        return await self._client.post("/api/client/statistics/phrases", json={
            "campaigns": campaigns, "dateFrom": date_from, "dateTo": date_to,
        })
