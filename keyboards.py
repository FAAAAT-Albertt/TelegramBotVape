"""Keyboards for Telegram bot"""
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup

async def start_keyboard() -> ReplyKeyboardMarkup:
    """Create started markup"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="Ассортимент🍏")
    builder.button(text="Моя корзина🛒")
    builder.button(text="Информация об оплатеℹ️")
    builder.button(text="Мои заказы📦")
    builder.button(text="Информация о доставкеℹ️")
    builder.button(text="Служба поддержки📞")
    builder.adjust(2,2,1,1)
    return builder.as_markup(resize_keyboard=True)
