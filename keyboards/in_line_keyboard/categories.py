from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import main_category_callback_data
from utils.db_api.main_db import Categories


def get_kb_categories():
    categ = Categories.select()
    keyboard = InlineKeyboardMarkup(row_width=2)
    for i in categ:
        print(i.category)
        keyboard.insert(InlineKeyboardButton(text=i.category, callback_data=main_category_callback_data.new(key=i.category)))
    return keyboard