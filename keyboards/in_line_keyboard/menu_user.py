from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import main_user_callback_data, test_del_callback_data, main_user_sub_alert_mes
from utils.db_api.models.user import User

inline_keyboard_main_user = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Стать пользователем?)', callback_data=main_user_callback_data.new(key='Add_user')),
        InlineKeyboardButton(text='Перестать быть польз.:(', callback_data='main_menu_user:Del_user'),
    ],
    [
        InlineKeyboardButton(text='Подписаться', callback_data=main_user_callback_data.new(key='Sub_user')),
        InlineKeyboardButton(text='Отписаться', callback_data='main_menu_user:Del_Sub_user'),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])

inline_keyboard_main_user_sub_alert_mes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Да', callback_data=main_user_sub_alert_mes.new(answer='OK')),
        InlineKeyboardButton(text='Нет', callback_data=main_user_sub_alert_mes.new(answer='NO'))
    ], [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]])


def get_10user():
    us = User.select().order_by(User.date_add).limit(10)
    return us


def get_kb_test():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        *[
            InlineKeyboardButton(
            text=f'{user.telegram_id}: {user.name}, {user.date_add}',
            callback_data=test_del_callback_data.new(key=user.telegram_id))
            for user in get_10user()
        ]
    )
    return keyboard