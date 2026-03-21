"""Сервис: Отзывы и рейтинг."""
from src.collectors.reviews.reviews import ReviewsCollector
from src.services.base import BaseService


class ReviewsService(BaseService):
    async def list_reviews(self, *, sort_dir: str = "DESC", limit: int = 100, offset: int = 0) -> dict:
        async with ReviewsCollector() as c:
            return await c.list_reviews(sort_dir=sort_dir, limit=limit, offset=offset)

    async def get_review(self, *, review_id: str) -> dict:
        async with ReviewsCollector() as c:
            return await c.get_review(review_id=review_id)

    async def leave_comment(self, *, review_id: str, text: str) -> dict:
        async with ReviewsCollector() as c:
            return await c.leave_comment(review_id=review_id, text=text)

    async def get_rating_summary(self) -> dict:
        async with ReviewsCollector() as c:
            return await c.get_rating_summary()
