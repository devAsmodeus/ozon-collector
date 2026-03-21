"""Ozon Performance API proxy: Рекламные кампании."""
from litestar import Controller, get, post
from src.services.performance.campaigns import PerformanceCampaignsService


class OzonPerformanceController(Controller):
    path = "/"
    tags = ["Реклама (Performance)"]

    @get("/campaigns", summary="Список рекламных кампаний (Performance API)")
    async def list_campaigns(self) -> dict:
        return await PerformanceCampaignsService().list_campaigns()

    @post("/campaigns/info", summary="Детали кампании (Performance API)")
    async def get_campaign(self, data: dict) -> dict:
        return await PerformanceCampaignsService().get_campaign(campaign_id=data["campaign_id"])

    @post("/campaigns/products", summary="Товары в кампании (Performance API)")
    async def get_campaign_products(self, data: dict) -> dict:
        return await PerformanceCampaignsService().get_campaign_products(campaign_id=data["campaign_id"])

    @post("/statistics/create", summary="Запросить отчёт статистики (Performance API)")
    async def create_statistics_report(self, data: dict) -> dict:
        return await PerformanceCampaignsService().create_statistics_report(
            campaigns=data["campaigns"], date_from=data["date_from"], date_to=data["date_to"],
            group_by=data.get("group_by", "DATE"),
        )

    @post("/statistics/get", summary="Получить отчёт по UUID (Performance API)")
    async def get_statistics_report(self, data: dict) -> dict:
        return await PerformanceCampaignsService().get_statistics_report(uuid=data["uuid"])

    @post("/statistics/phrases", summary="Статистика по фразам (Performance API)")
    async def get_phrase_statistics(self, data: dict) -> dict:
        return await PerformanceCampaignsService().get_phrase_statistics(
            campaigns=data["campaigns"], date_from=data["date_from"], date_to=data["date_to"],
        )
