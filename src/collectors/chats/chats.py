"""Коллектор: Чаты с покупателями."""
from src.collectors.base import OzonApiClient


class ChatsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_chats(self, *, filter: dict | None = None, limit: int = 100, offset: int = 0) -> dict:
        """POST /v3/chat/list — список чатов."""
        body = {"filter": filter or {}, "limit": limit, "offset": offset}
        return await self._client.post("/v3/chat/list", json=body)

    async def get_history(self, *, chat_id: str, limit: int = 100, offset: int = 0) -> dict:
        """POST /v3/chat/history — история сообщений."""
        return await self._client.post("/v3/chat/history", json={
            "chat_id": chat_id, "limit": limit, "offset": offset,
        })

    async def send_message(self, *, chat_id: str, text: str) -> dict:
        """POST /v1/chat/send/message — отправить сообщение."""
        return await self._client.post("/v1/chat/send/message", json={
            "chat_id": chat_id, "text": text,
        })

    async def start_chat(self, *, posting_number: str) -> dict:
        """POST /v1/chat/start — начать чат по отправлению."""
        return await self._client.post("/v1/chat/start", json={"posting_number": posting_number})

    async def mark_as_read(self, *, chat_id: str) -> dict:
        """POST /v1/chat/read — отметить чат прочитанным."""
        return await self._client.post("/v1/chat/read", json={"chat_id": chat_id})
