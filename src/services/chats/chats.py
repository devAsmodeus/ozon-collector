"""Сервис: Чаты с покупателями."""
from src.collectors.chats.chats import ChatsCollector
from src.services.base import BaseService


class ChatsService(BaseService):
    async def list_chats(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        async with ChatsCollector() as c:
            return await c.list_chats(filter=filter, limit=limit, offset=offset)

    async def get_history(self, *, chat_id: str, limit: int = 100, offset: int = 0) -> dict:
        async with ChatsCollector() as c:
            return await c.get_history(chat_id=chat_id, limit=limit, offset=offset)

    async def send_message(self, *, chat_id: str, text: str) -> dict:
        async with ChatsCollector() as c:
            return await c.send_message(chat_id=chat_id, text=text)

    async def start_chat(self, *, posting_number: str) -> dict:
        async with ChatsCollector() as c:
            return await c.start_chat(posting_number=posting_number)
