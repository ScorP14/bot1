from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import main_category_callback_data
from utils.db_api.models.categories import Categories


def get_kb_categories():
    cate = Categories.get_list_categories()
    keyboard = InlineKeyboardMarkup(row_width=3)
    for i in cate:
        keyboard.insert(InlineKeyboardButton(text=i,
                                             callback_data=main_category_callback_data.new(key=i)))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='test'))
    return keyboard


def get_one_categ(categor: str):
    try:
        categ = Categories.get_by_id(categor)
        return categ
    except Categories.DoesNotExist:
        return False



