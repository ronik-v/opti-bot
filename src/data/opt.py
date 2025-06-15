from logging import getLogger
from tinkoff.invest.async_services import AsyncServices
from tinkoff.invest import InstrumentStatus, OptionDirection, Option, OptionStyle


class OptionsService:
    def __init__(self, client: AsyncServices):
        self.client = client
        self.logger = getLogger(__name__)

    async def load_list(self) -> list[Option]:
        """CALL options list"""
        response = await self.client.instruments.options(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)

        return [
            option for option in response.instruments
            if (
                option.direction == OptionDirection.OPTION_DIRECTION_CALL and
                option.style == OptionStyle.OPTION_STYLE_EUROPEAN
            )
        ]

