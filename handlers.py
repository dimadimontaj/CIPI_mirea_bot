import asyncio
from aiogram import Bot
from aiogram.types import Message, FSInputFile, CallbackQuery
import emoji
import random

from keyboards import get_start_keyboard, get_jokes_keyboard
from callbackdata import CategoryInfo, RatingInfo
from db_api import quick_commands as commands


async def get_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=FSInputFile('media/kolobok.jpg'),
                         caption=emoji.emojize("Привет! Сегодня ты узнаешь много <b><s>АХУЕННЫХ</s></b> "
                                               "хороших анекдотов :rolling_on_the_floor_laughing:\n\n"
                                               "<b><s>РАСЧЕХЛЯЙ СВОЙ ПИВАС</s></b> Выбирай категорию и наслождайся!"),
                         has_spoiler=True,
                         reply_markup=get_start_keyboard())
    try:
        await message.delete()
    except Exception:
        pass


async def get_help(message: Message, bot: Bot):
    msg = await bot.send_message(chat_id=message.from_user.id, text=emoji.emojize("<b><s>КОЖАННЫЙ УБЛЮДОК</s></b> никакой помощи не будет :middle_finger:"))
    await message.delete()
    await asyncio.sleep(2)
    try:
        await msg.delete()
    except Exception:
        pass


async def get_jokes(call: CallbackQuery, callback_data: CategoryInfo):
    category = callback_data.category
    if category == 'all':
        jokes = await commands.select_all_jokes()
    else:
        jokes = await commands.select_category_jokes(category)
    try:
        joke = jokes[random.randint(0, len(jokes) - 1)]
        await call.message.edit_caption(caption=f'{joke.jokes} \n\n\nРейтинг анекдота: {joke.rating}', reply_markup=get_jokes_keyboard(category, joke.joke_id))
    except Exception:
        pass
    await call.answer('')


async def change_rating(call: CallbackQuery, callback_data: RatingInfo):
    changes = callback_data.changes
    joke_id = callback_data.joke_id
    await commands.change_rating(joke_id, changes)
    joke = await commands.select_joke(joke_id)
    await call.message.edit_caption(caption=f'{joke.jokes} \n\n\nРейтинг анекдота: {joke.rating}', reply_markup=get_jokes_keyboard(joke.category, joke.joke_id))
    await call.answer('оценка зарегистрирована')