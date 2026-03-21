"""Ozon API proxy: Отчёты — расширенные."""
from litestar import Controller, get, post
from src.services.reports_ext.reports import ReportsService


class OzonReportsController(Controller):
    path = "/"
    tags = ["Отчёты"]

    @post("/create", summary="Создать отчёт (Ozon API)")
    async def create_report(self, data: dict) -> dict:
        return await ReportsService().create_report(report_type=data["report_type"], params=data.get("params"))

    @post("/info", summary="Статус отчёта (Ozon API)")
    async def get_report_info(self, data: dict) -> dict:
        return await ReportsService().get_report_info(code=data["code"])

    @post("/list", summary="Список отчётов (Ozon API)")
    async def list_reports(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ReportsService().list_reports(page=params.get("page", 1), page_size=params.get("page_size", 100))

    @post("/realization", summary="Отчёт о реализации (Ozon API)")
    async def get_realization_report(self, data: dict) -> dict:
        return await ReportsService().get_realization_report(date=data["date"])

    @get("/rating", summary="Рейтинг продавца (Ozon API)")
    async def get_rating_summary(self) -> dict:
        return await ReportsService().get_rating_summary()
