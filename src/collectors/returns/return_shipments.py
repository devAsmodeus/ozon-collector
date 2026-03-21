"""Коллектор: Возвратные отгрузки — получение со складов Ozon."""
from src.collectors.base import OzonApiClient


class ReturnShipmentsCollector:
    def __init__(self):
        self._client = OzonApiClient()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._client.__aexit__(*args)

    async def is_giveout_enabled(self) -> dict:
        """POST /v1/return/giveout/is-enabled — доступен ли самовывоз возвратов."""
        return await self._client.post("/v1/return/giveout/is-enabled")

    async def list_giveout(self) -> dict:
        """POST /v1/return/giveout/list — список активных возвратов для выдачи."""
        return await self._client.post("/v1/return/giveout/list")

    async def get_giveout_info(self, *, return_id: int) -> dict:
        """POST /v1/return/giveout/info — детали возвратной отгрузки."""
        return await self._client.post("/v1/return/giveout/info", json={"return_id": return_id})

    async def get_giveout_barcode(self, *, return_id: int) -> dict:
        """POST /v1/return/giveout/barcode — штрихкод возвратной отгрузки."""
        return await self._client.post("/v1/return/giveout/barcode", json={"return_id": return_id})

    async def get_fbs_returns_info(self, *, posting_number: str) -> dict:
        """POST /v1/returns/company/fbs/info — информация о FBS возвратах."""
        return await self._client.post("/v1/returns/company/fbs/info", json={"posting_number": posting_number})

    # --- rFBS действия ---

    async def rfbs_reject(self, *, return_id: int, comment: str = "", reason_id: int = 0) -> dict:
        """POST /v2/returns/rfbs/reject — отклонить rFBS возврат. ⚠️ Мутация."""
        return await self._client.post("/v2/returns/rfbs/reject", json={
            "return_id": return_id, "comment": comment, "reason_id": reason_id,
        })

    async def rfbs_compensate(self, *, return_id: int, compensation_amount: float) -> dict:
        """POST /v2/returns/rfbs/compensate — частичная компенсация. ⚠️ Мутация."""
        return await self._client.post("/v2/returns/rfbs/compensate", json={
            "return_id": return_id, "compensation_amount": compensation_amount,
        })

    async def rfbs_verify(self, *, return_id: int) -> dict:
        """POST /v2/returns/rfbs/verify — подтвердить возврат на проверку. ⚠️ Мутация."""
        return await self._client.post("/v2/returns/rfbs/verify", json={"return_id": return_id})

    async def rfbs_receive_return(self, *, return_id: int) -> dict:
        """POST /v2/returns/rfbs/receive-return — подтвердить получение товара. ⚠️ Мутация."""
        return await self._client.post("/v2/returns/rfbs/receive-return", json={"return_id": return_id})

    async def rfbs_return_money(self, *, return_id: int) -> dict:
        """POST /v2/returns/rfbs/return-money — вернуть деньги покупателю. ⚠️ Мутация."""
        return await self._client.post("/v2/returns/rfbs/return-money", json={"return_id": return_id})
