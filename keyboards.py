"""Keyboards for Telegram bot"""
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.markdown import hbold, hitalic
# from database import database as base

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

async def prestart_keyboard() -> InlineKeyboardMarkup:
    """Create markup cities in the bot"""
    cities = await base.get_cities()
    builder = InlineKeyboardBuilder()
    for city in cities:
        builder.button(text=city['city'], callback_data=f"city_{city['id_city']}")
    builder.adjust(1)
    return builder.as_markup()

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
        builder.button(text=brand['brand'], callback_data=f"brand_{brand['brand']}_{category}")
    builder.button(text="Назад", callback_data='category')
    builder.adjust(1)
    return builder.as_markup()

async def first_goods_keyboard(brand, category) -> (str, str, InlineKeyboardMarkup):
    """Create markup for first goods"""
    goods = await base.get_first_of_goods(category, brand)
    text_caption = hbold(goods[0]['name']) + "\nЦена: " + hitalic(f"{goods[0]['price']}р.")
    image = f"jpg/{goods[0]['image']}"
    builder = InlineKeyboardBuilder()
    builder.button(text="<--", callback_data="None")
    builder.button(text=str(goods[0]['count']), callback_data="None")
    if len(goods) > 1:
        builder.button(text="-->", callback_data=f"next_goods_{goods[1]['id_catalog']}")
    else:
        builder.button(text="-->", callback_data="None")
    builder.button(text="Добавить в корзину", callback_data=f"add_card_{goods[0]['id_catalog']}")
    builder.button(text="Назад", callback_data=f"return_cat_{category}")
    builder.adjust(3,1,1)
    return image, text_caption, builder.as_markup()

async def goods_keyboard(id_catalog) -> (str, str, InlineKeyboardMarkup):
    """Create markup for first goods"""
    goods, category = await base.get_goods_by_id(id_catalog)
    index = 0
    for good in goods:
        if good['id_catalog'] == int(id_catalog):
            text_caption = hbold(good['name']) + "\nЦена: " + hitalic(f"{good['price']}р.")
            image = f"jpg/{good['image']}"
            builder = InlineKeyboardBuilder()
            if index == 0:
                builder.button(text="<--", callback_data="None")
            else:
                builder.button(text="<--",
                               callback_data=f"prev_goods_{goods[index - 1]['id_catalog']}")
            builder.button(text=str(good['count']), callback_data="None")
            if index == len(goods) - 1:
                builder.button(text="-->", callback_data="None")
            else:
                builder.button(text="-->",
                               callback_data=f"next_goods_{goods[index + 1]['id_catalog']}")
            builder.button(text="Добавить в корзину", callback_data=f"add_card_{id_catalog}")
            builder.button(text="Назад", callback_data=f"return_cat_{category}")
            builder.adjust(3,1,1)
            return image, text_caption, builder.as_markup()
        index += 1

async def feedback_keyboard() -> InlineKeyboardMarkup:
    """Create feedback markup"""
    builder = InlineKeyboardBuilder()
    builder.button(text="Ответить", callback_data="admin_answer")

    return builder.as_markup()