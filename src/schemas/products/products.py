"""Схемы: Товары — список и информация."""
from pydantic import BaseModel


class ProductListFilter(BaseModel):
    """Фильтр для POST /v2/product/list."""
    offer_id: list[str] | None = None
    product_id: list[int] | None = None
    visibility: str = "ALL"


class ProductListRequest(BaseModel):
    filter: ProductListFilter = ProductListFilter()
    last_id: str = ""
    limit: int = 100


class ProductItem(BaseModel):
    product_id: int
    offer_id: str = ""


class ProductListResponse(BaseModel):
    items: list[ProductItem] = []
    total: int = 0
    last_id: str = ""


class ProductInfoItem(BaseModel):
    id: int
    name: str = ""
    offer_id: str = ""
    barcode: str = ""
    category_id: int = 0
    description_category_id: int = 0
    type_id: int = 0
    created_at: str = ""
    sku: int = 0
    fbs_sku: int = 0
    marketing_price: str = ""
    min_price: str = ""
    old_price: str = ""
    price: str = ""
    currency_code: str = ""
    images: list | None = None
    attributes: list | None = None
    sources: list | None = None
    stocks: dict | None = None
    visibility_details: dict | None = None
    is_archived: bool = False
    is_autoarchived: bool = False
    is_prepayment: bool = False
    is_prepayment_allowed: bool = False
    status: dict | None = None


class ProductInfoResponse(BaseModel):
    items: list[ProductInfoItem] = []
