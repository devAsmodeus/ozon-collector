"""Схемы: Аналитика продавца."""
from pydantic import BaseModel


class AnalyticsDataRequest(BaseModel):
    """Запрос POST /v1/analytics/data."""
    date_from: str
    date_to: str
    metrics: list[str] = [
        "revenue",
        "ordered_units",
        "returns_units",
        "session_view",
        "hits_view",
        "conv_tocart_pdp",
    ]
    dimension: list[str] = ["sku"]
    filters: list[dict] | None = None
    sort: list[dict] | None = None
    limit: int = 1000
    offset: int = 0


class AnalyticsDataRow(BaseModel):
    dimensions: list[dict] = []
    metrics: list[float] = []


class AnalyticsDataResponse(BaseModel):
    result: dict = {}
    timestamp: str = ""
