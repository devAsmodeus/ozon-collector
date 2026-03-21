"""Схемы: Товары — Цены."""
from pydantic import BaseModel


class PriceFilterRequest(BaseModel):
    """Запрос цен POST /v4/product/info/prices."""
    filter: dict | None = None
    last_id: str = ""
    limit: int = 100


class PriceItem(BaseModel):
    product_id: int = 0
    offer_id: str = ""
    price: dict | None = None
    old_price: str = ""
    min_price: str = ""
    marketing_price: str = ""
    marketing_seller_price: str = ""
    currency_code: str = ""
    vat: str = ""
    price_index: str = ""
    auto_action_enabled: bool = False
    commission_amount: float = 0
    commission_percent: float = 0
    volume_weight: float = 0


class PriceListResponse(BaseModel):
    items: list[PriceItem] = []
    last_id: str = ""
    total: int = 0
