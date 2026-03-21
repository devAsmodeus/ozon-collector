"""Коллектор: FBS действия — отгрузка, акты, этикетки, статусы."""
from src.collectors.base import OzonApiClient


class FbsActionsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    # --- Отгрузка ---

    async def ship_posting(self, *, posting_number: str, packages: list[dict]) -> dict:
        """POST /v4/posting/fbs/ship — отгрузить отправление. ⚠️ Мутация."""
        return await self._client.post("/v4/posting/fbs/ship", json={
            "posting_number": posting_number, "packages": packages,
        })

    async def cancel_posting(self, *, posting_number: str, cancel_reason_id: int, cancel_reason_message: str = "") -> dict:
        """POST /v2/posting/fbs/cancel — отменить отправление. ⚠️ Мутация."""
        return await self._client.post("/v2/posting/fbs/cancel", json={
            "posting_number": posting_number,
            "cancel_reason_id": cancel_reason_id,
            "cancel_reason_message": cancel_reason_message,
        })

    # --- Статусы ---

    async def set_delivering(self, *, posting_number: list[str]) -> dict:
        """POST /v2/fbs/posting/delivering — перевести в 'доставляется'."""
        return await self._client.post("/v2/fbs/posting/delivering", json={"posting_number": posting_number})

    async def set_delivered(self, *, posting_number: list[str]) -> dict:
        """POST /v2/fbs/posting/delivered — перевести в 'доставлено'."""
        return await self._client.post("/v2/fbs/posting/delivered", json={"posting_number": posting_number})

    async def set_last_mile(self, *, posting_number: list[str]) -> dict:
        """POST /v2/fbs/posting/last-mile — перевести в 'последняя миля'."""
        return await self._client.post("/v2/fbs/posting/last-mile", json={"posting_number": posting_number})

    async def set_tracking_number(self, *, posting_number: str, tracking_number: str) -> dict:
        """POST /v2/posting/fbs/tracking-number/set — установить трек-номер."""
        return await self._client.post("/v2/posting/fbs/tracking-number/set", json={
            "posting_number": posting_number, "tracking_number": tracking_number,
        })

    # --- Акты ---

    async def create_act(self, *, delivery_method_id: int, departure_date: str) -> dict:
        """POST /v2/posting/fbs/act/create — создать акт приёма-передачи."""
        return await self._client.post("/v2/posting/fbs/act/create", json={
            "delivery_method_id": delivery_method_id, "departure_date": departure_date,
        })

    async def check_act_status(self, *, id: int) -> dict:
        """POST /v2/posting/fbs/act/check-status — статус генерации акта."""
        return await self._client.post("/v2/posting/fbs/act/check-status", json={"id": id})

    async def get_act_barcode(self, *, id: int) -> dict:
        """POST /v2/posting/fbs/act/get-barcode — получить штрихкод акта."""
        return await self._client.post("/v2/posting/fbs/act/get-barcode", json={"id": id})

    async def get_act_postings(self, *, id: int) -> dict:
        """POST /v2/posting/fbs/act/get-postings — отправления в акте."""
        return await self._client.post("/v2/posting/fbs/act/get-postings", json={"id": id})

    # --- Этикетки ---

    async def get_package_label(self, *, posting_number: list[str]) -> dict:
        """POST /v2/posting/fbs/package-label — этикетки отправлений."""
        return await self._client.post("/v2/posting/fbs/package-label", json={"posting_number": posting_number})

    # --- Страна производства ---

    async def get_product_country_list(self, *, posting_number: str) -> dict:
        """POST /v2/posting/fbs/product/country/list — список стран производства."""
        return await self._client.post("/v2/posting/fbs/product/country/list", json={"posting_number": posting_number})

    async def set_product_country(self, *, posting_number: str, items: list[dict]) -> dict:
        """POST /v2/posting/fbs/product/country/set — установить страну. ⚠️ Мутация."""
        return await self._client.post("/v2/posting/fbs/product/country/set", json={
            "posting_number": posting_number, "items": items,
        })
