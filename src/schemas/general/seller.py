"""Схемы: Общее — Информация о продавце Ozon."""
from pydantic import BaseModel


class SellerInfo(BaseModel):
    """Информация о продавце."""
    name: str
    company_id: str
