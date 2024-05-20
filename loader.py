from aiogram import Bot

from config import admins


async def start_bot(bot: Bot):
    for admin in admins:
        await bot.send_message(chat_id=admin, text='хуйня активировалась')


async def stop_bot(bot: Bot):
    for admin in admins:
        await bot.send_message(chat_id=admin, text='хуйня закончила работу')