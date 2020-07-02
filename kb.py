from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = InlineKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            inline_keyboard=[
    [
        InlineKeyboardButton(text='Пук1', callback_data='1'),
        InlineKeyboardButton(text='Пук2', callback_data='2'),
        InlineKeyboardButton(text='Пук3', callback_data='3')
    ],
    [
        InlineKeyboardButton(text='Пук4',callback_data='4')
    ]
])


test_mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [
        KeyboardButton(text='pyk1'),
        KeyboardButton(text='pyk2'),
        KeyboardButton(text='pyk3')
    ],
    [
        KeyboardButton(text='pyk4')
    ]
])
