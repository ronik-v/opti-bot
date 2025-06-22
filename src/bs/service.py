from typing import override
from logging import getLogger

from tinkoff.invest import Option
from tinkoff.invest.async_services import AsyncServices

from src.bs.abstract import BsServiceAbstract, OptionStockData, ModelCallResult
from src.core.data import OptionsStockService


class BsService(BsServiceAbstract):
    def __init__(self, client: AsyncServices):
        self.client = client

        self.data = OptionsStockService(self.client)
        self.logger = getLogger(__name__)

    @override
    def send_model_results(self, uid_calls: ModelCallResult) -> None:
        """TODO"""

    @override
    def model_results(self, data: OptionStockData) -> ModelCallResult:
        """TODO"""

    @override
    async def options_and_stocks_data(self) -> OptionStockData:
        """Options and close prices stock data"""
        options: list[Option] = await self.data.load_options_list()
        stock_prices: dict[str, list[float]] = await self.data.load_stock_prices(
            [option.basic_asset for option in options]
        )
