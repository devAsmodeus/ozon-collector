"""Ozon API proxy: Отзывы и рейтинг."""
from litestar import Controller, get, post
from src.services.reviews.reviews import ReviewsService


class OzonReviewsController(Controller):
    path = "/"
    tags = ["Отзывы"]

    @post("/list", summary="Список отзывов (Ozon API)")
    async def list_reviews(self, data: dict | None = None) -> dict:
        params = data or {}
        return await ReviewsService().list_reviews(sort_dir=params.get("sort_dir", "DESC"), limit=params.get("limit", 100))

    @post("/info", summary="Детали отзыва (Ozon API)")
    async def get_review(self, data: dict) -> dict:
        return await ReviewsService().get_review(review_id=data["review_id"])

    @post("/comment", summary="Ответить на отзыв (Ozon API)")
    async def leave_comment(self, data: dict) -> dict:
        return await ReviewsService().leave_comment(review_id=data["review_id"], text=data["text"])

    @get("/rating", summary="Рейтинг продавца (Ozon API)")
    async def get_rating_summary(self) -> dict:
        return await ReviewsService().get_rating_summary()
