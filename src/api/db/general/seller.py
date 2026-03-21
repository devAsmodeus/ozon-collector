"""DB: General / Продавец — чтение из БД."""
from litestar import Controller, get

from src.schemas.general.seller import SellerInfo
from src.utils.db_manager import DBManager


class DbSellerController(Controller):
    path = "/seller"
    tags = ["DB / General"]

    @get(
        "/info",
        summary="Информация о продавце из БД",
        description="Читает последние сохранённые данные продавца из локальной БД.",
    )
    async def get_seller_info(self, db: DBManager) -> SellerInfo:
        sellers = await db.seller.get_all()
        if sellers:
            return sellers[0]
        from src.exceptions import ObjectNotFoundException
        raise ObjectNotFoundException("Seller not found in DB. Run /sync/general/seller/info first.")
