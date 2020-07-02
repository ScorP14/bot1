from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from db.main_db import User, get_user_by_id


def get_keyboard(id_tg):

    user = get_user_by_id(id_tg)
    if not user:
        user = User()
    kb = ReplyKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             keyboard=[
                                 [
                                     KeyboardButton('/help'),
                                     KeyboardButton('/check'),
                                     KeyboardButton('/add') if not user.telegram_id else KeyboardButton('/del'),
                                     KeyboardButton('/subt') if not user.sub else KeyboardButton('/subf')
                                 ],
                                 [
                                     KeyboardButton('Cancel')
                                 ]
                             ])
    return kb


keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='Пук1', callback_data='1'),
                                             InlineKeyboardButton(text='Пук2', callback_data='2'),
                                             InlineKeyboardButton(text='Пук3', callback_data='3')
                                         ],
                                         [
                                             InlineKeyboardButton(text='Пук4', callback_data='4')
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
