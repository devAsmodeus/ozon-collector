"""ORM модели: Маркетинг и акции Ozon."""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Integer, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonPromotion(Base):
    """Акция Ozon (Hot Sale, промокоды и т.д.)."""
    __tablename__ = "ozon_promotions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    action_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID акции")
    title: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Название акции")
    action_type: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Тип акции")
    description: Mapped[str | None] = mapped_column(String(2000), nullable=True, comment="Описание")
    date_start: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата начала")
    date_end: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата окончания")
    freeze_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата заморозки")
    is_participating: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Участвует продавец")
    participating_products_count: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Кол-во товаров в акции")
    potential_products_count: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Потенциальные товары")
    banned_products_count: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Заблокированные товары")
    products: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Товары в акции")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
