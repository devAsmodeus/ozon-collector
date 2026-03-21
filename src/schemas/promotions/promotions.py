"""Схемы: Акции и промо."""
from pydantic import BaseModel


class PromotionItem(BaseModel):
    id: int
    title: str = ""
    action_type: str = ""
    description: str = ""
    date_start: str = ""
    date_end: str = ""
    freeze_date: str = ""
    is_participating: bool = False
    participating_products_count: int = 0
    potential_products_count: int = 0
    banned_products_count: int = 0


class PromotionListResponse(BaseModel):
    result: list[PromotionItem] = []


class PromotionProductsRequest(BaseModel):
    action_id: int
    limit: int = 100
    offset: int = 0


class PromotionProductItem(BaseModel):
    id: int = 0
    price: float = 0
    action_price: float = 0
    max_action_price: float = 0
    add_mode: str = ""
    stock: int = 0


class PromotionProductsResponse(BaseModel):
    result: dict = {}
