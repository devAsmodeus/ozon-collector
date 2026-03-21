"""ORM модели: Товары Ozon — карточки, цены, остатки, склады."""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Float, Integer, Numeric, String, DateTime, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class OzonProduct(Base):
    """Карточка товара Ozon."""
    __tablename__ = "ozon_products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID товара в Ozon")
    offer_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True, comment="Артикул продавца")
    name: Mapped[str | None] = mapped_column(String(1000), nullable=True, comment="Название товара")
    barcode: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="Штрихкод")
    category_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID категории")
    description_category_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID описательной категории")
    type_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID типа товара")
    created_at: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Дата создания товара")
    sku: Mapped[int | None] = mapped_column(BigInteger, nullable=True, index=True, comment="SKU (FBO)")
    fbs_sku: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="SKU (FBS)")
    marketing_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Цена до маркетинговых акций")
    min_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Минимальная цена")
    old_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Цена до скидки")
    price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Текущая цена")
    currency_code: Mapped[str | None] = mapped_column(String(10), nullable=True, comment="Код валюты")
    is_prepayment: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Предоплата")
    is_prepayment_allowed: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Предоплата разрешена")
    images: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Изображения товара")
    attributes: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Атрибуты товара")
    sources: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Источники товара")
    stocks: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Остатки (summary)")
    visibility_details: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Детали видимости")
    is_archived: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="В архиве")
    is_autoarchived: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Автоархивация")
    status: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="Статусы модерации и валидации")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonPrice(Base):
    """Цена товара Ozon."""
    __tablename__ = "ozon_prices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, comment="ID товара")
    offer_id: Mapped[str | None] = mapped_column(String(255), nullable=True, comment="Артикул продавца")
    price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Цена с учётом скидок")
    old_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Цена до скидки")
    min_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Минимальная цена")
    marketing_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Маркетинговая цена")
    marketing_seller_price: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Цена для продавца в акции")
    currency_code: Mapped[str | None] = mapped_column(String(10), nullable=True, comment="Валюта")
    vat: Mapped[str | None] = mapped_column(String(20), nullable=True, comment="Ставка НДС")
    price_index: Mapped[str | None] = mapped_column(String(20), nullable=True, comment="Ценовой индекс")
    auto_action_enabled: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Автоакция включена")
    commission_amount: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True, comment="Сумма комиссии")
    commission_percent: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True, comment="Процент комиссии")
    volume_weight: Mapped[float | None] = mapped_column(Float, nullable=True, comment="Объёмный вес, кг")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonStock(Base):
    """Остаток товара на складах Ozon."""
    __tablename__ = "ozon_stocks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, comment="ID товара")
    offer_id: Mapped[str | None] = mapped_column(String(255), nullable=True, comment="Артикул продавца")
    stock_type: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Тип склада (fbo/fbs)")
    present: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Доступно на складе")
    reserved: Mapped[int | None] = mapped_column(Integer, nullable=True, comment="Зарезервировано")
    warehouse_name: Mapped[str | None] = mapped_column(String(255), nullable=True, comment="Название склада")
    warehouse_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="ID склада")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")


class OzonWarehouse(Base):
    """Склад продавца Ozon."""
    __tablename__ = "ozon_warehouses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    warehouse_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True, comment="ID склада")
    name: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Название склада")
    is_rfbs: Mapped[bool | None] = mapped_column(Boolean, nullable=True, comment="Склад rFBS")
    status: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="Статус склада")
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, comment="Дата синхронизации")
