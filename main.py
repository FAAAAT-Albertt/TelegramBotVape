"""Telegram Bot"""
import asyncio
# import datetime
# import json

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
#from aiogram.utils.markdown import hbold, hitalic, hlink
import config
import keyboards

dp = Dispatcher()
bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Answer to /start"""
    await message.answer("Выберите действие", reply_markup=await keyboards.start_keyboard())

# @dp.message(F.text == 'Загрузить')
# async def download_price(message: Message):
#     await message.reply("Успешно!")

async def start():
    """Start Telegram Bot"""
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
