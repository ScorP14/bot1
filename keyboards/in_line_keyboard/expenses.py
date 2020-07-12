from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import main_expenses_callback_data, main_category_callback_data
from utils.db_api.models.models import User, Expenses

in_keyboard_main_expenses = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Добавить расход', callback_data=main_expenses_callback_data.new(id='Add_exp')),
        InlineKeyboardButton(text='Удалить', callback_data=main_expenses_callback_data.new(id='Del_exp')),
    ],
    [
        InlineKeyboardButton(text='<<< Назад', callback_data=main_expenses_callback_data.new(id='Back_exp')),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])














inline_keyboard_main_category = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Все расходы', callback_data=main_category_callback_data.new(key='All_exp')),
        InlineKeyboardButton(text='Последние 5 расходов', callback_data=main_category_callback_data.new(key='Last_5_exp')),
    ],
    [
        InlineKeyboardButton(text='Расход за день', callback_data=main_category_callback_data.new(key='Day_exp')),
        InlineKeyboardButton(text='Расход за неделю', callback_data=main_category_callback_data.new(key='Medely_exp'))
    ],
    [
        InlineKeyboardButton(text='Расход за месяц', callback_data=main_category_callback_data.new(key='Monz_exp')),
        InlineKeyboardButton(text='Расход за год', callback_data=main_category_callback_data.new(key='Year_exp')),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])


def get_keyboard_expense():
    user = User.get_user(468933460)
    expens = Expenses.select().where(Expenses.user == user)
    keyIN = InlineKeyboardMarkup(row_width=2)
    for i in expens:
        keyIN.add(InlineKeyboardButton(text=f'{i.id}: {i.category.category} - {i.text_mes}',
                                       callback_data=main_expenses_callback_data.new(id=i.id)))

    return keyIN

