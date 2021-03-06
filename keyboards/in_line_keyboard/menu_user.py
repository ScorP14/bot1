from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.callback import cdb_menu_user, cdb_user_sub_alert_mes, cdb_menu_user_sub


in_kb_main_user = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Стать пользователем?)', callback_data=cdb_menu_user.new(key='Add_user')),
     InlineKeyboardButton(text='Перестать быть польз.:(', callback_data='cdb_menu_user:Del_user')],

    [InlineKeyboardButton(text='Подписка', callback_data=cdb_menu_user.new(key='Sub_user')),
     InlineKeyboardButton(text='<<< Назад', callback_data=cdb_menu_user.new(key='Back'))],

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
