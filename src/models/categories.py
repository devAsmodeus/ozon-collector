"""ORM модели: Категории и атрибуты Ozon."""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Integer, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonCategory(Base):
    """Категория товаров Ozon (description_category)."""
    __tablename__ = "ozon_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    description_category_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID категории")
    category_name: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Название категории")
    parent_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID родительской категории")
    disabled: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Категория отключена")
    children: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Дочерние категории")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
