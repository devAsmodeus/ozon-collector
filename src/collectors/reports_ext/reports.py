"""Коллектор: Отчёты — расширенные."""
from src.collectors.base import OzonApiClient


class ReportsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def create_report(self, *, report_type: str, params: dict | None = None) -> dict:
        """POST /v1/report/create — создать отчёт."""
        body = {"report_type": report_type}
        if params:
            body.update(params)
        return await self._client.post("/v1/report/create", json=body)

    async def get_report_info(self, *, code: str) -> dict:
        """POST /v1/report/info — статус и ссылка на отчёт."""
        return await self._client.post("/v1/report/info", json={"code": code})

    async def list_reports(self, *, page: int = 1, page_size: int = 100, report_type: str = "") -> dict:
        """POST /v1/report/list — список отчётов."""
        body = {"page": page, "page_size": page_size}
        if report_type:
            body["report_type"] = report_type
        return await self._client.post("/v1/report/list", json=body)

    async def get_realization_report(self, *, date: dict) -> dict:
        """POST /v2/finance/realization — отчёт о реализации."""
        return await self._client.post("/v2/finance/realization", json={"date": date})

    async def get_rating_summary(self) -> dict:
        """POST /v1/rating/summary — рейтинг продавца."""
        return await self._client.post("/v1/rating/summary")
