from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import cdb_menu_category, cdb_menu_exp_from_category_paginate
from states.state import PaginatorForExpenses
from utils.db_api.models.func_model_categories import get_list_categories, get_category_from_str
from utils.db_api.models.func_model_view_expenses import get_name_expenses_from_category_generator, \
    get_name_expenses_from_category_paginator
from utils.db_api.models.models import Categories


def get_kb_categories():
    list_category = get_list_categories()
    keyboard = InlineKeyboardMarkup(row_width=3)
    for i in list_category:
        keyboard.insert(InlineKeyboardButton(text=i,
                                             callback_data=cdb_menu_category.new(key=i)))
    keyboard.add(InlineKeyboardButton(text='<<< Назад', callback_data=cdb_menu_category.new(key='Back')))
    keyboard.add(InlineKeyboardButton(text='Выход', callback_data=cdb_menu_category.new(key='Exit')))
    return keyboard



def test():
    category_1 = get_category_from_str('Продукты')
    expenses = get_name_expenses_from_category_paginator(category_1, 1, 3)
    for i in expenses:
        print(i)

# PaginatorForExpenses()


def get_kb_expenses_from_category_paginator(category: str):
    category_1 = get_category_from_str(category)
    expenses = get_name_expenses_from_category_generator(category_1)
    keyboard = InlineKeyboardMarkup(row_width=4, inline_keyboard=[[
        InlineKeyboardButton(text='<Назад',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Expenses_paginator_back')),
        InlineKeyboardButton(text='Вперед>',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Expenses_paginator_next'))]]
                                    )
    keyboard.add(*[InlineKeyboardButton(text=i.title(), callback_data=cdb_menu_category.new(key=i))
                   for i in expenses])
    keyboard.row(
        InlineKeyboardButton(text='Добавить категорию расхода',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Add_category_exp')),
        InlineKeyboardButton(text='<<< Назад',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Back_exp')),
        InlineKeyboardButton(text='Выход',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Exit'))
    )
    return keyboard




def get_kb_expenses_from_category(category: str):
    category_1 = get_category_from_str(category)
    expenses = get_name_expenses_from_category_generator(category_1)
    keyboard = InlineKeyboardMarkup(row_width=4, inline_keyboard=[[
        InlineKeyboardButton(text='<Назад',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Expenses_paginator_back')),
        InlineKeyboardButton(text='Вперед>',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Expenses_paginator_next'))]]
                                    )
    keyboard.add(*[InlineKeyboardButton(text=i.title(), callback_data=cdb_menu_category.new(key=i))
                   for i in expenses])
    keyboard.row(
        InlineKeyboardButton(text='Добавить категорию расхода',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Add_category_exp')),
        InlineKeyboardButton(text='<<< Назад',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Back_exp')),
        InlineKeyboardButton(text='Выход',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Exit'))
    )
    return keyboard


def get_one_category(category: str):
    try:
        item = Categories.get_by_id(category)
        return item
    except Categories.DoesNotExist:
        return False


def test12312(expenses):
    keyboard = InlineKeyboardMarkup(row_width=4, inline_keyboard=[[
        InlineKeyboardButton(text='<Назад',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Expenses_paginator_back')),
        InlineKeyboardButton(text='Вперед>',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Expenses_paginator_next'))]]
                                    )
    keyboard.add(*[InlineKeyboardButton(text=str(i).title(), callback_data=cdb_menu_category.new(key=i))
                   for i in expenses])
    keyboard.row(
        InlineKeyboardButton(text='Добавить категорию расхода',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Add_category_exp')),
        InlineKeyboardButton(text='<<< Назад',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Back_exp')),
        InlineKeyboardButton(text='Выход',
                             callback_data=cdb_menu_exp_from_category_paginate.new(key='Exit'))
    )
    return keyboard
