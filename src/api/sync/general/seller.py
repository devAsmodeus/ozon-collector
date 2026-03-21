"""Sync: General / Продавец — сохранение в БД."""
from litestar import Controller, post

from src.schemas.general.seller import SellerInfo
from src.services.general.seller import SellerService
from src.utils.db_manager import DBManager


class SyncSellerController(Controller):
    path = "/seller"
    tags = ["Sync / General"]

    @post(
        "/info",
        summary="Синхронизация информации о продавце",
        description="Получает данные из Ozon API и сохраняет в БД.",
    )
    async def sync_seller_info(self, db: DBManager) -> SellerInfo:
        return await SellerService(db=db).sync_seller_info()
