"""Keyboards for Telegram bot"""
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from database import database as base

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

async def categories_keyboard() -> InlineKeyboardMarkup:
    """Create categories markup"""
    categories = await base.get_unique_categories()
    builder = InlineKeyboardBuilder()
    for category in categories:
        builder.button(text=category['category'], callback_data=f"cat_{category['category']}")
    builder.button(text="Назад", callback_data='start')
    builder.adjust(1)
    return builder.as_markup()

async def brand_keyboard(category) -> InlineKeyboardMarkup:
    """Create brand markup"""
    brands = await base.get_unique_brand(category)
    builder = InlineKeyboardBuilder()
    for brand in brands:
        builder.button(text=brand['brand'], callback_data=f"brand_{brand['brand']}")
    builder.button(text="Назад", callback_data='category')
    builder.adjust(1)
    return builder.as_markup()
