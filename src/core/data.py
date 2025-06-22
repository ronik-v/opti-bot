from datetime import datetime, timedelta, UTC
from tinkoff.invest.async_services import AsyncServices
from tinkoff.invest import InstrumentStatus, OptionDirection, Option, OptionStyle, InstrumentIdType, CandleInterval


class OptionsStockService:
    def __init__(self, client: AsyncServices):
        self.client = client
        self.to_date = datetime.now(UTC)
        self.from_date = self.to_date - timedelta(days=7)

    async def load_options_list(self) -> list[Option]:
        """CALL options list"""
        response = await self.client.instruments.options(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)

        return [
            option for option in response.instruments
            if (
                option.direction == OptionDirection.OPTION_DIRECTION_CALL and
                option.style == OptionStyle.OPTION_STYLE_EUROPEAN
            )
        ]

    async def load_stock_prices(self, ticker_list: list[str]) -> dict[str, list[float]]:
        """Stock prices"""
        result: dict[str, list[float]] = {}
        for ticker in ticker_list:
            figi = (await self.client.instruments.find_instrument(
                ticker=ticker,
                instrument_id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER
            )).instruments[0].figi

            candles = await self.client.market_data.get_candles(
                figi=figi,
                from_=self.from_date.isoformat(),
                to=self.to_date.isoformat(),
                interval=CandleInterval.CANDLE_INTERVAL_HOUR
            )

            result[ticker] = [c.close.units + c.close.nano / 1e9 for c in candles.candles]

        return result
