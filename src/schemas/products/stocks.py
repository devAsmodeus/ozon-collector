"""Схемы: Товары — Остатки и склады."""
from pydantic import BaseModel


class StockInfoRequest(BaseModel):
    """Запрос остатков POST /v3/product/info/stocks."""
    filter: dict | None = None
    last_id: str = ""
    limit: int = 100


class StockItem(BaseModel):
    product_id: int = 0
    offer_id: str = ""
    stocks: list[dict] = []


class StockInfoResponse(BaseModel):
    items: list[StockItem] = []
    last_id: str = ""
    total: int = 0


class WarehouseItem(BaseModel):
    warehouse_id: int
    name: str = ""
    is_rfbs: bool = False
    status: str = ""


class WarehouseListResponse(BaseModel):
    result: list[WarehouseItem] = []
