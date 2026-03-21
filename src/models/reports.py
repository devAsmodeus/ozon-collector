"""ORM модели: Финансы и аналитика Ozon."""
from datetime import datetime

from sqlalchemy import BigInteger, Float, Integer, Numeric, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonTransaction(Base):
    """Финансовая транзакция Ozon (из /v3/finance/transaction/list)."""
    __tablename__ = "ozon_transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    operation_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID операции")
    operation_type: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Тип операции")
    operation_type_name: Mapped[str | None] = mapped_column(String(255), nullable=True, comment="Название типа")
    operation_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, index=True, comment="Дата операции")
    accruals_for_sale: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Начисления за продажу")
    sale_commission: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Комиссия за продажу")
    amount: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Сумма операции")
    delivery_charge: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Стоимость доставки")
    return_delivery_charge: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Стоимость обратной доставки")
    posting_number: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True, comment="Номер отправления")
    items: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Товары [{name, sku}]")
    services: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Сервисные начисления")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonAnalyticsData(Base):
    """Аналитика продавца (из /v1/analytics/data)."""
    __tablename__ = "ozon_analytics_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True, comment="Дата данных")
    dimensions: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Размерности (sku, category, ...)")
    metrics: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Метрики (revenue, orders, ...)")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
