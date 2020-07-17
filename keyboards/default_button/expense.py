from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


rasxod = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = KeyboardButton(text='Отмена')
rasxod.add(btn1)



message_y_n = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_1 = KeyboardButton(text='Да')
btn_2 = KeyboardButton(text='Отмена')
message_y_n.add(btn_1, btn_2)
