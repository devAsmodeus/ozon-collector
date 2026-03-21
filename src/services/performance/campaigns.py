"""Сервис: Performance API — рекламные кампании."""
from src.collectors.performance.campaigns import CampaignsCollector
from src.services.base import BaseService


class PerformanceCampaignsService(BaseService):
    async def list_campaigns(self) -> dict:
        async with CampaignsCollector() as c:
            return await c.list_campaigns()

    async def get_campaign(self, *, campaign_id: int) -> dict:
        async with CampaignsCollector() as c:
            return await c.get_campaign(campaign_id=campaign_id)

    async def get_campaign_products(self, *, campaign_id: int) -> dict:
        async with CampaignsCollector() as c:
            return await c.get_campaign_products(campaign_id=campaign_id)

    async def create_statistics_report(self, *, campaigns: list[int], date_from: str, date_to: str, group_by: str = "DATE") -> dict:
        async with CampaignsCollector() as c:
            return await c.create_statistics_report(campaigns=campaigns, date_from=date_from, date_to=date_to, group_by=group_by)

    async def get_statistics_report(self, *, uuid: str) -> dict:
        async with CampaignsCollector() as c:
            return await c.get_statistics_report(uuid=uuid)

    async def get_phrase_statistics(self, *, campaigns: list[int], date_from: str, date_to: str) -> dict:
        async with CampaignsCollector() as c:
            return await c.get_phrase_statistics(campaigns=campaigns, date_from=date_from, date_to=date_to)
