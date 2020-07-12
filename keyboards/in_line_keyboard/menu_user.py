from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import test_del_callback_data, cdb_menu_user, cdb_user_sub_alert_mes, \
    cdb_menu_user_sub
from utils.db_api.models.models import User

in_kb_main_user = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Стать пользователем?)', callback_data=cdb_menu_user.new(key='Add_user')),
     InlineKeyboardButton(text='Перестать быть польз.:(', callback_data='cdb_menu_user:Del_user')],

    [InlineKeyboardButton(text='Подписка', callback_data=cdb_menu_user.new(key='Sub_user')),
     InlineKeyboardButton(text='Назад', callback_data=cdb_menu_user.new(key='Back'))],

    [InlineKeyboardButton(text='Выход', callback_data=cdb_menu_user.new(key='Exit'))]
])


in_kb_user_sub = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подписаться', callback_data=cdb_menu_user_sub.new(key='User_sub_true')),
     InlineKeyboardButton(text='Отписаться', callback_data=cdb_menu_user_sub.new(key='User_sub_false'))],

    [InlineKeyboardButton(text='Отмена', callback_data=cdb_menu_user_sub.new(key='Cancel'))]])




in_kb_sub_alert_mes = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data=cdb_user_sub_alert_mes.new(answer='OK')),
     InlineKeyboardButton(text='Нет', callback_data=cdb_user_sub_alert_mes.new(answer='NO'))],

    [InlineKeyboardButton(text='Отмена', callback_data=cdb_user_sub_alert_mes.new(answer='Cancel'))]])


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