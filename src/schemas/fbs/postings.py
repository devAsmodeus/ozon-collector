"""Схемы: Заказы FBS — отправления."""
from pydantic import BaseModel


class FbsPostingFilter(BaseModel):
    since: str = ""
    to: str = ""
    status: str = ""


class FbsPostingListRequest(BaseModel):
    dir: str = "ASC"
    filter: FbsPostingFilter = FbsPostingFilter()
    limit: int = 50
    offset: int = 0
    with_: dict | None = None

    class Config:
        populate_by_name = True


class FbsPostingItem(BaseModel):
    posting_number: str
    order_id: int = 0
    order_number: str = ""
    status: str = ""
    substatus: str = ""
    in_process_at: str = ""
    shipment_date: str = ""
    delivering_date: str = ""
    cancel_reason_id: int = 0
    cancellation_type: str = ""
    delivery_method: dict | None = None
    tracking_number: str = ""
    tpl_integration_type: str = ""
    products: list[dict] = []
    analytics_data: dict | None = None
    financial_data: dict | None = None
    is_express: bool = False
    is_multibox: bool = False
    multi_box_qty: int = 0


class FbsPostingListResponse(BaseModel):
    result: dict = {}
