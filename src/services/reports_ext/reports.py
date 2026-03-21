"""Сервис: Отчёты — расширенные."""
from src.collectors.reports_ext.reports import ReportsCollector
from src.services.base import BaseService


class ReportsService(BaseService):
    async def create_report(self, *, report_type: str, params: dict | None = None) -> dict:
        async with ReportsCollector() as c:
            return await c.create_report(report_type=report_type, params=params)

    async def get_report_info(self, *, code: str) -> dict:
        async with ReportsCollector() as c:
            return await c.get_report_info(code=code)

    async def list_reports(self, *, page: int = 1, page_size: int = 100, report_type: str = "") -> dict:
        async with ReportsCollector() as c:
            return await c.list_reports(page=page, page_size=page_size, report_type=report_type)

    async def get_realization_report(self, *, date: dict) -> dict:
        async with ReportsCollector() as c:
            return await c.get_realization_report(date=date)

    async def get_rating_summary(self) -> dict:
        async with ReportsCollector() as c:
            return await c.get_rating_summary()
