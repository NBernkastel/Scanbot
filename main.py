import asyncio
import logging
import sys

from src.config.bot_config import dp, bot
from src.routers.qr_router import qr_router


async def start():
    dp.include_routers(qr_router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())