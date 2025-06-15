from contextlib import asynccontextmanager

from tinkoff.invest.async_services import AsyncServices
from tinkoff.invest.clients import AsyncClient

from src.core.config import config


@asynccontextmanager
async def get_exchange_client() -> AsyncServices:
    """Exchange API client"""
    async with AsyncClient(config.API_TOKEN) as client:
        yield client
