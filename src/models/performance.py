"""ORM модели: Performance API — рекламные кампании."""
from datetime import datetime

from sqlalchemy import BigInteger, Float, Integer, Numeric, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonCampaign(Base):
    """Рекламная кампания Ozon Performance."""
    __tablename__ = "ozon_campaigns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    campaign_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID кампании")
    title: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Название кампании")
    state: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True, comment="Статус кампании")
    adv_object_type: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Тип рекламного объекта")
    daily_budget: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Дневной бюджет")
    from_date: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата начала")
    to_date: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата окончания")
    created_at: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата создания")
    updated_at: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата обновления")
    products: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Товары в кампании")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Полные данные кампании")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonCampaignStat(Base):
    """Статистика рекламной кампании."""
    __tablename__ = "ozon_campaign_stats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    campaign_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, comment="ID кампании")
    report_uuid: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="UUID отчёта")
    report_date: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True, comment="Дата отчёта")
    views: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="Показы")
    clicks: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Клики")
    ctr: Mapped[float | None] = mapped_column(Float, nullable=True, comment="CTR %")
    cpc: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="CPC руб.")
    spend: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Расход руб.")
    orders: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Заказы")
    revenue: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Выручка руб.")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Полные данные статистики")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
