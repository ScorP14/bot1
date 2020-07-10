from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


rasxod = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = KeyboardButton(text='Отмена')
rasxod.add(btn1)
