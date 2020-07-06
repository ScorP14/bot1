from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import main_user_callback_data


inline_keyboard_main_category = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Все расходы', callback_data=main_user_callback_data.new(key='Add')),
        InlineKeyboardButton(text='Последние 5 расходов', callback_data='main_menu_user:Del'),
    ],
    [
        InlineKeyboardButton(text='Расход за день', callback_data=main_user_callback_data.new(key='Sub')),
        InlineKeyboardButton(text='Расход за неделю', callback_data='main_menu_user:Del_Sub')
    ],
    [
        InlineKeyboardButton(text='Расход за месяц', callback_data='main_menu_user:Del_Sub'),
        InlineKeyboardButton(text='Расход за год', callback_data='main_menu_user:Del_Sub'),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])