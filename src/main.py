from asyncio import run

from src.core.exchange_client import get_exchange_client
from src.data.opt import OptionsService


async def main() -> None:
    async with get_exchange_client() as client:
        opt_service = OptionsService(client)
        opt_list = await opt_service.load_list()
        print(f"RESULT({type(opt_list)}) = {opt_list}, \nRESULT{({type(opt_list)})} - {type(opt_list[0])})")


if __name__ == "__main__":
    run(main())
