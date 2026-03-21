"""Коллектор: Отзывы и рейтинг."""
from src.collectors.base import OzonApiClient


class ReviewsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def list_reviews(self, *, sort_dir: str = "DESC", limit: int = 100, offset: int = 0) -> dict:
        """POST /v1/review/list — список отзывов."""
        return await self._client.post("/v1/review/list", json={
            "sort_dir": sort_dir, "limit": limit, "offset": offset,
        })

    async def get_review(self, *, review_id: str) -> dict:
        """POST /v1/review/info — детали отзыва."""
        return await self._client.post("/v1/review/info", json={"review_id": review_id})

    async def leave_comment(self, *, review_id: str, text: str) -> dict:
        """POST /v1/review/comment/create — ответить на отзыв."""
        return await self._client.post("/v1/review/comment/create", json={
            "review_id": review_id, "text": text,
        })

    async def delete_comment(self, *, review_id: str, comment_id: str) -> dict:
        """POST /v1/review/comment/delete — удалить ответ на отзыв."""
        return await self._client.post("/v1/review/comment/delete", json={
            "review_id": review_id, "comment_id": comment_id,
        })

    async def get_rating_summary(self) -> dict:
        """POST /v1/rating/summary — сводка по рейтингу продавца."""
        return await self._client.post("/v1/rating/summary")
