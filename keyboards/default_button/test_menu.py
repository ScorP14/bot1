from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


test_mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [
        KeyboardButton(text='/add'),
        KeyboardButton(text='/del'),
        KeyboardButton(text='/sub'),
        KeyboardButton(text='/check'),
    ],
    [
        KeyboardButton(text='/cancel')
    ]
])