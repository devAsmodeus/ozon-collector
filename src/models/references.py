"""ORM модели: Справочники — состояние синхронизации."""
from datetime import datetime

from sqlalchemy import BigInteger, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonSyncState(Base):
    """Состояние синхронизации по модулям."""
    __tablename__ = "ozon_sync_state"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    module: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True, comment="Название модуля синхронизации")
    last_sync_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, comment="Последняя успешная синхронизация")
    last_cursor: Mapped[str | None] = mapped_column(String(255), nullable=True, comment="Курсор пагинации")
    records_total: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="Всего записей в БД")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="ok / error / running")
    error_message: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Сообщение об ошибке")
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, comment="Дата обновления")
