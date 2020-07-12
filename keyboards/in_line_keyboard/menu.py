from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.callback_data.callback import cbd_menu

in_kb_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Пользователь',
                             callback_data=cbd_menu.new(key='User')),
        InlineKeyboardButton(text='Категории', callback_data='cbd_menu:Category'),
    ],
    [
        InlineKeyboardButton(text='Расходы',
                             callback_data=cbd_menu.new(key='Expenses'))
    ],
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])