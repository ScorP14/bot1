from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from utils.db_api.main_db import User


def get_keyboard(id_tg):
    user = User.get_or_none(id_tg)
    if not user:
        user = User()
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
        [
            KeyboardButton('/help'),
            KeyboardButton('/check'),
            KeyboardButton('/add') if not user.telegram_id else KeyboardButton('/del'),
            KeyboardButton('/subt') if not user.sub else KeyboardButton('/subf')
        ], [KeyboardButton('Cancel')]])
    return kb

