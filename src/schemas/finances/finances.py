"""Схемы: Финансы — транзакции."""
from pydantic import BaseModel


class TransactionListFilter(BaseModel):
    date: dict | None = None
    operation_type: list[str] | None = None
    posting_number: str = ""
    transaction_type: str = "all"


class TransactionListRequest(BaseModel):
    filter: TransactionListFilter = TransactionListFilter()
    page: int = 1
    page_size: int = 100


class TransactionItem(BaseModel):
    operation_id: int
    operation_type: str = ""
    operation_type_name: str = ""
    operation_date: str = ""
    accruals_for_sale: float = 0
    sale_commission: float = 0
    amount: float = 0
    delivery_charge: float = 0
    return_delivery_charge: float = 0
    posting: dict | None = None
    items: list[dict] = []
    services: list[dict] = []


class TransactionListResponse(BaseModel):
    result: dict = {}
