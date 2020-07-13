from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import cdb_menu_category
from utils.db_api.models.func_model_categories import get_list_categories
from utils.db_api.models.models import Categories


def get_kb_categories():
    list_category = get_list_categories()
    keyboard = InlineKeyboardMarkup(row_width=3)
    for i in list_category:
        keyboard.insert(InlineKeyboardButton(text=i,
                                             callback_data=cdb_menu_category.new(key=i)))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data=cdb_menu_category.new(key='Back')))
    keyboard.add(InlineKeyboardButton(text='Выход', callback_data=cdb_menu_category.new(key='Exit')))
    return keyboard


def get_one_category(category: str):
    try:
        item = Categories.get_by_id(category)
        return item
    except Categories.DoesNotExist:
        return False
