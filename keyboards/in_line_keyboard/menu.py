from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.callback_data.callback import main_callback_data


inline_keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Пользователь',
                             callback_data=main_callback_data.new(key='User')),
        InlineKeyboardButton(text='Категории', callback_data='main_menu:Category'),
    ],
    [
        InlineKeyboardButton(text='Расходы',
                             callback_data=main_callback_data.new(key='Expenses'))
    ],
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])
