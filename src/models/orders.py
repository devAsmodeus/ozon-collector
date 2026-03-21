"""ORM модели: Заказы Ozon — FBS и FBO postings."""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Integer, Numeric, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class FbsPosting(Base):
    """Отправление FBS (сборочное задание)."""
    __tablename__ = "ozon_fbs_postings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    posting_number: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True, comment="Номер отправления")
    order_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, index=True, comment="ID заказа")
    order_number: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Номер заказа")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True, comment="Статус отправления")
    substatus: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Подстатус")
    in_process_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата принятия в обработку")
    shipment_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата отгрузки")
    delivering_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата доставки")
    cancel_reason_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID причины отмены")
    cancellation_type: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Тип отмены")
    delivery_method: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Способ доставки")
    tracking_number: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Трек-номер")
    tpl_integration_type: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Тип интеграции с ТПЛ")
    products: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Товары в отправлении [{sku, name, quantity, offer_id, price, ...}]")
    analytics_data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Аналитика: регион, город, способ доставки")
    financial_data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Финансовые данные: комиссии, выплаты")
    is_express: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Экспресс-доставка")
    is_multibox: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Многокоробочное отправление")
    multi_box_qty: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Количество коробок")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class FboPosting(Base):
    """Отправление FBO (с склада Ozon)."""
    __tablename__ = "ozon_fbo_postings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    posting_number: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True, comment="Номер отправления")
    order_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, index=True, comment="ID заказа")
    order_number: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Номер заказа")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True, comment="Статус")
    cancel_reason_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID причины отмены")
    created_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата создания")
    in_process_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата принятия в обработку")
    products: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Товары [{sku, name, quantity, offer_id, price}]")
    analytics_data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Аналитика")
    financial_data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Финансовые данные")
    additional_data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Доп. данные")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
