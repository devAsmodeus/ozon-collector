from litestar import Router
from src.api.ozon.chats.chats import OzonChatsController
ozon_chats_router = Router(path="/chats", route_handlers=[OzonChatsController])
