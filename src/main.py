"""Точка входа — Litestar приложение."""
import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from litestar import Litestar, get
from litestar.config.cors import CORSConfig
from litestar.contrib.prometheus import PrometheusConfig, PrometheusController
from litestar.di import Provide
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar.openapi.spec import Components, SecurityScheme, Tag

from src.dependencies import provide_db_manager, provide_db_session
from src.exceptions import EXCEPTION_HANDLERS
from src.init import redis_manager
from src.logging_config import setup_logging

setup_logging(level="INFO")
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Lifespan
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(_: Litestar) -> AsyncGenerator[None, None]:
    await redis_manager.connect()
    logger.info("Ozon Collector started", extra={"event": "startup"})
    yield
    await redis_manager.close()
    logger.info("Ozon Collector stopped", extra={"event": "shutdown"})


# ---------------------------------------------------------------------------
# Системные роуты
# ---------------------------------------------------------------------------

@get("/health", tags=["System"], summary="Проверка работоспособности сервиса")
async def health() -> dict:
    return {"status": "ok", "version": "0.1.0"}


# ---------------------------------------------------------------------------
# Роутеры
# ---------------------------------------------------------------------------

from src.api.ozon import ozon_router
from src.api.sync import sync_router
from src.api.db import db_router

# ---------------------------------------------------------------------------
# Приложение
# ---------------------------------------------------------------------------

prometheus_config = PrometheusConfig(
    app_name="ozon_collector",
    prefix="ozon_collector_http",
    labels={"app": "ozon-collector"},
)

app = Litestar(
    route_handlers=[
        health,
        PrometheusController,
        ozon_router,
        sync_router,
        db_router,
    ],
    lifespan=[lifespan],
    dependencies={
        "db_session": Provide(provide_db_session),
        "db": Provide(provide_db_manager),
    },
    exception_handlers=EXCEPTION_HANDLERS,
    middleware=[prometheus_config.middleware],
    openapi_config=OpenAPIConfig(
        title="Ozon Collector",
        version="0.1.0",
        description=(
            "Сбор и аналитика данных Ozon Seller API.\n\n"
            "**Ozon API** — прямые прокси к Ozon API с сохранением в БД.\n"
            "**Sync** — синхронизация данных в БД.\n"
            "**DB** — чтение данных из локальной БД.\n\n"
            "**Авторизация:** Client-Id + Api-Key заголовки к Ozon Seller API."
        ),
        components=Components(
            security_schemes={
                "OzonAuth": SecurityScheme(
                    type="apiKey",
                    security_scheme_in="header",
                    name="Api-Key",
                    description="Ozon Seller API ключ (Api-Key заголовок).",
                )
            }
        ),
        security=[{"OzonAuth": []}],
        render_plugins=[SwaggerRenderPlugin(version="5.18.2", js_url=None, css_url=None)],
        path="/docs",
        tags=[
            Tag(name="System", description="Служебные эндпоинты"),
            Tag(name="Ozon / General", description="Прокси к Ozon API / Общее"),
            Tag(name="Sync / General", description="Синхронизация в БД / Общее"),
            Tag(name="DB / General", description="Данные из БД / Общее"),
            Tag(name="Products — Карточки", description="Ozon API / Товары / Карточки"),
            Tag(name="Products — Цены", description="Ozon API / Товары / Цены и скидки"),
            Tag(name="Products — Остатки", description="Ozon API / Товары / Остатки и склады"),
            Tag(name="Отправления FBS", description="Ozon API / Заказы FBS / Отправления"),
            Tag(name="Отправления FBO", description="Ozon API / Заказы FBO / Отправления"),
            Tag(name="FBS Действия", description="Ozon API / FBS / Отгрузка, акты, этикетки"),
            Tag(name="Поставки FBO", description="Ozon API / Заявки на поставку FBO"),
            Tag(name="Аналитика", description="Ozon API / Аналитика продавца"),
            Tag(name="Финансы", description="Ozon API / Финансы / Транзакции"),
            Tag(name="Отчёты", description="Ozon API / Отчёты / Создание, статус, реализация"),
            Tag(name="Акции", description="Ozon API / Маркетинг / Акции и промо"),
            Tag(name="Категории", description="Ozon API / Категории, атрибуты, справочники"),
            Tag(name="Сертификаты", description="Ozon API / Сертификаты качества и брендов"),
            Tag(name="Штрихкоды", description="Ozon API / Генерация и привязка штрихкодов"),
            Tag(name="Возвраты", description="Ozon API / Возвраты FBO и rFBS"),
            Tag(name="Отмены", description="Ozon API / Запросы на отмену заказов"),
            Tag(name="Отзывы", description="Ozon API / Отзывы покупателей, рейтинг"),
            Tag(name="Чаты", description="Ozon API / Чаты с покупателями"),
            Tag(name="Ценовые стратегии", description="Ozon API / Автоматическое ценообразование"),
            Tag(name="Реклама (Performance)", description="Ozon Performance API / Кампании, ставки, статистика"),
        ],
    ),
    cors_config=CORSConfig(allow_origins=["*"]),
)
