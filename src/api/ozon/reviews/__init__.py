from litestar import Router
from src.api.ozon.reviews.reviews import OzonReviewsController
ozon_reviews_router = Router(path="/reviews", route_handlers=[OzonReviewsController])
