from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class SellerOrm(Base):
    """Информация о продавце Ozon."""
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), comment="Название компании")
    company_id: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, comment="ID компании в Ozon",
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
