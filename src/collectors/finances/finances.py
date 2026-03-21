"""Коллектор: Финансы — транзакции."""
from src.collectors.base import OzonApiClient


class FinancesCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def get_transaction_list(
        self,
        *,
        filter: dict | None = None,
        page: int = 1,
        page_size: int = 100,
    ) -> dict:
        """POST /v3/finance/transaction/list — список транзакций."""
        body = {
            "filter": filter or {"transaction_type": "all"},
            "page": page,
            "page_size": page_size,
        }
        return await self._client.post("/v3/finance/transaction/list", json=body)

    async def get_totals(self) -> dict:
        """POST /v1/finance/cash-flow-statement/list — итоги по финансам."""
        return await self._client.post("/v1/finance/cash-flow-statement/list")
