"""DB router — /db/* (чтение данных из локальной БД)."""
from litestar import Router

from src.api.db.general import db_general_router

db_router = Router(
    path="/db",
    route_handlers=[db_general_router],
)
