"""ORM модели: Ценовые стратегии."""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Integer, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonStrategy(Base):
    """Ценовая стратегия."""
    __tablename__ = "ozon_strategies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    strategy_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID стратегии")
    name: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Название стратегии")
    strategy_type: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Тип стратегии")
    enabled: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Включена")
    products_count: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Кол-во товаров")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Полные данные стратегии")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
