"""Сервис: FBS действия."""
from src.collectors.fbs_actions.actions import FbsActionsCollector
from src.services.base import BaseService


class FbsActionsService(BaseService):
    async def ship_posting(self, *, posting_number: str, packages: list[dict]) -> dict:
        async with FbsActionsCollector() as c:
            return await c.ship_posting(posting_number=posting_number, packages=packages)

    async def create_act(self, *, delivery_method_id: int, departure_date: str) -> dict:
        async with FbsActionsCollector() as c:
            return await c.create_act(delivery_method_id=delivery_method_id, departure_date=departure_date)

    async def check_act_status(self, *, id: int) -> dict:
        async with FbsActionsCollector() as c:
            return await c.check_act_status(id=id)

    async def get_package_label(self, *, posting_number: list[str]) -> dict:
        async with FbsActionsCollector() as c:
            return await c.get_package_label(posting_number=posting_number)

    async def set_delivering(self, *, posting_number: list[str]) -> dict:
        async with FbsActionsCollector() as c:
            return await c.set_delivering(posting_number=posting_number)

    async def set_delivered(self, *, posting_number: list[str]) -> dict:
        async with FbsActionsCollector() as c:
            return await c.set_delivered(posting_number=posting_number)
