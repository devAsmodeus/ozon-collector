"""Ozon API proxy: Чаты."""
from litestar import Controller, post
from src.services.chats.chats import ChatsService


class OzonChatsController(Controller):
    path = "/"
    tags = ["Чаты"]

    @post("/list", summary="Список чатов (Ozon API)")
    async def list_chats(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ChatsService().list_chats(filter=params.get("filter"), limit=params.get("limit", 100))

    @post("/history", summary="История чата (Ozon API)")
    async def get_history(self, data: dict) -> dict:
        return await ChatsService().get_history(chat_id=data["chat_id"], limit=data.get("limit", 100))

    @post("/send", summary="Отправить сообщение (Ozon API)")
    async def send_message(self, data: dict) -> dict:
        return await ChatsService().send_message(chat_id=data["chat_id"], text=data["text"])

    @post("/start", summary="Начать чат по отправлению (Ozon API)")
    async def start_chat(self, data: dict) -> dict:
        return await ChatsService().start_chat(posting_number=data["posting_number"])
