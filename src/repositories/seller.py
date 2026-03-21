from sqlalchemy.dialects.postgresql import insert

from src.models.seller import SellerOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import SellerMapper


class SellerRepository(BaseRepository):
    model = SellerOrm
    mapper = SellerMapper

    async def upsert(self, data):
        stmt = (
            insert(SellerOrm)
            .values(
                name=data.name,
                company_id=data.company_id,
            )
            .on_conflict_do_update(
                index_elements=["company_id"],
                set_=dict(
                    name=data.name,
                ),
            )
            .returning(SellerOrm)
        )
        result = await self.session.execute(stmt)
        return self.mapper.map_to_domain_entity(result.scalars().one())
