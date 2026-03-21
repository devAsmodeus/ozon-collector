"""ORM модели: Сертификаты."""
from datetime import datetime

from sqlalchemy import BigInteger, Integer, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonCertificate(Base):
    """Сертификат качества / бренда."""
    __tablename__ = "ozon_certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    certificate_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID сертификата")
    name: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Название")
    certificate_type: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Тип сертификата")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Статус")
    issue_date: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата выдачи")
    expire_date: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата истечения")
    products: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Привязанные товары")
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Полные данные сертификата")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
