"""ORM модели: Коммуникации — отзывы, чаты, возвраты, отмены."""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Integer, String, DateTime, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonReview(Base):
    """Отзыв покупателя."""
    __tablename__ = "ozon_reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    review_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True, comment="ID отзыва")
    product_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, index=True, comment="ID товара")
    sku: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="SKU товара")
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Оценка (1-5)")
    text: Mapped[str | None] = mapped_column(Text, nullable=True, comment="Текст отзыва")
    comment: Mapped[str | None] = mapped_column(Text, nullable=True, comment="Ответ продавца")
    photos: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Фото отзыва")
    created_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата отзыва")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonChat(Base):
    """Чат с покупателем."""
    __tablename__ = "ozon_chats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chat_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True, comment="ID чата")
    chat_type: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Тип чата")
    posting_number: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Номер отправления")
    unread_count: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Непрочитанные сообщения")
    last_message_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата последнего сообщения")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Данные чата")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonReturn(Base):
    """Возврат товара."""
    __tablename__ = "ozon_returns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    return_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID возврата")
    posting_number: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True, comment="Номер отправления")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Статус возврата")
    return_reason_name: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Причина возврата")
    product_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID товара")
    sku: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="SKU")
    quantity: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Количество")
    returned_to_ozon_moment: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Дата возврата на склад Ozon")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Полные данные возврата")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonCancellation(Base):
    """Запрос на отмену заказа."""
    __tablename__ = "ozon_cancellations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cancellation_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID отмены")
    posting_number: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True, comment="Номер отправления")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Статус отмены")
    cancellation_type: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Тип отмены")
    cancel_reason: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Причина отмены")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Полные данные отмены")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
