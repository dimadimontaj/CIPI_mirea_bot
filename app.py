import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command

import config
from callbackdata import CategoryInfo, RatingInfo
from db_api.db_gino import on_startup_db
from handlers import change_rating, get_help, get_jokes, get_start
from loader import start_bot, stop_bot


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )

    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    await on_startup_db(dp)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands="start"))
    dp.message.register(get_help, Command(commands="help"))

    dp.callback_query.register(get_jokes, CategoryInfo.filter())
    dp.callback_query.register(get_start, F.data == "main_menu")
    dp.callback_query.register(change_rating, RatingInfo.filter())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
