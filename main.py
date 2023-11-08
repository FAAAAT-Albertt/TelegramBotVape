"""Telegram Bot"""
import asyncio
# import datetime
# import json
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import exceptions
#from aiogram.utils.markdown import hbold, hitalic, hlink
import config
import keyboards

dp = Dispatcher()
bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Answer to /start"""
    await message.answer("Выберите действие", reply_markup=await keyboards.start_keyboard())

@dp.message(F.text == 'Ассортимент🍏')
async def catalog(message: Message):
    """Answer to Ассортимент🍏"""
    await message.answer("Выберите категорию", reply_markup=await keyboards.categories_keyboard())
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)

@dp.callback_query(F.data.startswith("cat_"))
async def brand(callback: CallbackQuery):
    data = callback.data.replace('cat_', '')
    

async def start():
    """Start Telegram Bot"""
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
