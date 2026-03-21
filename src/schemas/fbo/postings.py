"""Схемы: Заказы FBO — отправления."""
from pydantic import BaseModel


class FboPostingFilter(BaseModel):
    since: str = ""
    to: str = ""
    status: str = ""


class FboPostingListRequest(BaseModel):
    dir: str = "ASC"
    filter: FboPostingFilter = FboPostingFilter()
    limit: int = 50
    offset: int = 0
    with_: dict | None = None


class FboPostingItem(BaseModel):
    posting_number: str
    order_id: int = 0
    order_number: str = ""
    status: str = ""
    cancel_reason_id: int = 0
    created_at: str = ""
    in_process_at: str = ""
    products: list[dict] = []
    analytics_data: dict | None = None
    financial_data: dict | None = None
    additional_data: list[dict] | None = None


class FboPostingListResponse(BaseModel):
    result: list[FboPostingItem] = []
