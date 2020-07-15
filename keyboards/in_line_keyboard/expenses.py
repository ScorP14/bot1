from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import cdb_menu_expenses, cdb_menu_category
from utils.db_api.models.models import Users, Expenses

in_keyboard_main_expenses = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Добавить расход', callback_data=cdb_menu_expenses.new(key='Add_exp')),
        InlineKeyboardButton(text='Просмотреть', callback_data=cdb_menu_expenses.new(key='View_exp')),
        InlineKeyboardButton(text='Удалить', callback_data=cdb_menu_expenses.new(key='Del_exp')),
    ],
    [
        InlineKeyboardButton(text='<<< Назад', callback_data=cdb_menu_expenses.new(key='Back_exp')),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])














inline_keyboard_main_category = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Все расходы', callback_data=cdb_menu_category.new(key='All_exp')),
        InlineKeyboardButton(text='Последние 5 расходов', callback_data=cdb_menu_category.new(key='Last_5_exp')),
    ],
    [
        InlineKeyboardButton(text='Расход за день', callback_data=cdb_menu_category.new(key='Day_exp')),
        InlineKeyboardButton(text='Расход за неделю', callback_data=cdb_menu_category.new(key='Medely_exp'))
    ],
    [
        InlineKeyboardButton(text='Расход за месяц', callback_data=cdb_menu_category.new(key='Monz_exp')),
        InlineKeyboardButton(text='Расход за год', callback_data=cdb_menu_category.new(key='Year_exp')),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])


def get_keyboard_expense():
    user = Users.get_user(468933460)
    expens = Expenses.select().where(Expenses.user == user)
    keyIN = InlineKeyboardMarkup(row_width=2)
    for i in expens:
        keyIN.add(InlineKeyboardButton(text=f'{i.id}: {i.category.category} - {i.text_mes}',
                                       callback_data=cdb_menu_expenses.new(id=i.id)))

    return keyIN
