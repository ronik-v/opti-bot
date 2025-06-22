from abc import ABC, abstractmethod
from tinkoff.invest import Option

from src.core.types import TradeSignal

type StockVolatile = float
type OptionUID = str
type OptionStockData = dict[OptionUID, tuple[list[Option]], StockVolatile]
type ModelCallResult = dict[OptionUID, TradeSignal]


class BsServiceAbstract(ABC):
    """Model for bs service"""
    @abstractmethod
    async def options_and_stocks_data(self) -> OptionStockData:
        raise NotImplemented()

    @abstractmethod
    def model_results(self, data: OptionStockData) -> ModelCallResult:
        raise NotImplemented()

    @abstractmethod
    def send_model_results(self, uid_calls: ModelCallResult) -> None:
        raise NotImplemented()
