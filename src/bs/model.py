from math import log, sqrt, exp, erf


def stock_volatile(close_prices: list[float]) -> float:
    log_income: list[float] = [
        log(close_prices[day_index] / close_prices[day_index - 1])
        for day_index in range(1, len(close_prices))
    ]
    log_len: int = len(log_income)
    log_income_mean: float = sum(log_income) / log_len

    return sqrt(
        (1 / (log_len - 1)) * sum([(log_income_val - log_income_mean) ** 2 for log_income_val in log_income])
    )


class OptionCallPriceModel:
    """Bs model for europe CALL option"""

    def __init__(
            self, current_price: float, strike: float, risk_free_rate: float,
            stock_volatility: float, time_to_expiration: float = 1 / 365
    ) -> None:
        self.S = current_price
        self.K = strike
        self.r = risk_free_rate
        self.sigma = stock_volatility
        self.T = time_to_expiration

    def option_price(self) -> float:
        """Theoretic CALL option price"""
        d1: float = self._d1()
        d2: float = self._d2(d1)

        return (
            self.S * self._phi(d1) - self.K * exp(-self.r * self.T) * self._phi(d2)
        )

    def _d1(self) -> float:
        return (
                log(self.S / self.K)
                + (self.r + 0.5 * self.sigma ** 2) * self.T
        ) / (self.sigma * sqrt(self.T))

    def _d2(self, d1: float) -> float:
        return d1 - self.sigma * sqrt(self.T)

    @staticmethod
    def _phi(x: float) -> float:
        return 0.5 * (1 + erf(x / sqrt(2)))
