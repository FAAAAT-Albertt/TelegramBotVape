"""Telegram Bot"""
import asyncio
# import datetime
# import json
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
#from aiogram.utils.markdown import hbold, hitalic, hlink
import config
import keyboards

dp = Dispatcher()
bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Answer to /start"""
    await message.answer("Выберите нужную кнопку", reply_markup=await keyboards.start_keyboard())

@dp.message(F.text == 'Ассортимент🍏')
async def catalog(message: Message):
    """Answer to Ассортимент🍏"""
    await message.answer("Выберите категорию", reply_markup=await keyboards.categories_keyboard())
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)

@dp.callback_query(F.data == 'start')
async def start_message(callback: CallbackQuery):
    """Callback to start message"""
    await callback.message.delete()
    await callback.message.answer("Выберите нужную кнопку",
                                  reply_markup=await keyboards.start_keyboard())

@dp.callback_query(F.data.startswith("cat_"))
async def brand(callback: CallbackQuery):
    """Callback from category"""
    data = callback.data.replace('cat_', '')
    await callback.message.edit_text("Выберите подкатегорию",
                                    reply_markup=await keyboards.brand_keyboard(data))

@dp.callback_query(F.data.startswith("return_cat_"))
async def return_brand(callback: CallbackQuery):
    """Callback from goods"""
    data = callback.data.replace('return_cat_', '')
    await callback.message.delete()
    await callback.message.answer("Выберите подкатегорию",
                                    reply_markup=await keyboards.brand_keyboard(data))

@dp.callback_query(F.data == 'category')
async def category_message(callback: CallbackQuery):
    """Callback to category message"""
    await callback.message.delete()
    await callback.message.answer("Выберите категорию",
                                  reply_markup=await keyboards.categories_keyboard())

@dp.callback_query(F.data.startswith("brand_"))
async def goods(callback: CallbackQuery):
    """Callback from category"""
    data = callback.data.replace('brand_', '')
    data = data.split('_')
    image, text_caption, markup = await keyboards.first_goods_keyboard(data[0], data[1])
    await callback.message.delete()
    await callback.message.answer_photo(photo=FSInputFile(image),
                                        caption=text_caption, reply_markup=markup)

@dp.callback_query(F.data.startswith("next_goods_"))
async def next_goods(callback: CallbackQuery):
    """Callback next goods"""
    data = callback.data.replace('next_goods_', '')
    image, text_caption, markup = await keyboards.goods_keyboard(data)
    await callback.message.delete()
    await callback.message.answer_photo(photo=FSInputFile(image),
                                        caption=text_caption, reply_markup=markup)

@dp.callback_query(F.data.startswith("prev_goods_"))
async def prev_goods(callback: CallbackQuery):
    """Callback previous goods"""
    data = callback.data.replace('prev_goods_', '')
    image, text_caption, markup = await keyboards.goods_keyboard(data)
    await callback.message.delete()
    await callback.message.answer_photo(photo=FSInputFile(image),
                                        caption=text_caption, reply_markup=markup)

async def start():
    """Start Telegram Bot"""
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
