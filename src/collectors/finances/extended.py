"""Коллектор: Финансы — расширенные отчёты."""
from src.collectors.base import OzonApiClient


class FinancesExtendedCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_transaction_totals(self, *, filter: dict | None = None) -> dict:
        """POST /v3/finance/transaction/totals — итого по транзакциям."""
        return await self._client.post("/v3/finance/transaction/totals", json={"filter": filter or {}})

    async def get_realization(self, *, date: dict) -> dict:
        """POST /v2/finance/realization — отчёт о реализации."""
        return await self._client.post("/v2/finance/realization", json={"date": date})

    async def get_realization_by_posting(self, *, posting_number: str) -> dict:
        """POST /v1/finance/realization/posting — реализация по отправлению."""
        return await self._client.post("/v1/finance/realization/posting", json={"posting_number": posting_number})

    async def get_mutual_settlement(self, *, date: dict) -> dict:
        """POST /v1/finance/mutual-settlement — взаиморасчёты."""
        return await self._client.post("/v1/finance/mutual-settlement", json={"date": date})

    async def get_cash_flow_statement(self, *, date: dict) -> dict:
        """POST /v1/finance/cash-flow-statement/list — ДДС отчёт."""
        return await self._client.post("/v1/finance/cash-flow-statement/list", json={"date": date})

    async def get_compensation(self, *, filter: dict | None = None) -> dict:
        """POST /v1/finance/compensation — компенсации."""
        return await self._client.post("/v1/finance/compensation", json={"filter": filter or {}})

    async def get_b2b_sales(self, *, filter: dict | None = None) -> dict:
        """POST /v1/finance/document-b2b-sales — продажи юрлицам."""
        return await self._client.post("/v1/finance/document-b2b-sales", json={"filter": filter or {}})
