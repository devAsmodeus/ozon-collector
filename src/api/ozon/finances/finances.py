"""Ozon API proxy: Финансы."""
from litestar import Controller, get, post

from src.services.finances.finances import FinancesService


class OzonFinancesController(Controller):
    path = "/"
    tags = ["Финансы"]

    @post(
        "/transactions",
        summary="Список транзакций (Ozon API)",
        description="**Ozon:** `POST /v3/finance/transaction/list`",
    )
    async def get_transaction_list(self, data: dict | None = None) -> dict:
        params = data or {}
        return await FinancesService().get_transaction_list(
            filter=params.get("filter"),
            page=params.get("page", 1),
            page_size=params.get("page_size", 100),
        )

    @get(
        "/totals",
        summary="Итоги по финансам (Ozon API)",
        description="**Ozon:** `POST /v1/finance/cash-flow-statement/list`",
    )
    async def get_totals(self) -> dict:
        return await FinancesService().get_totals()
