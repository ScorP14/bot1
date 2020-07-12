from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default_button.test_menu import test_mk
from keyboards.in_line_keyboard.menu import inline_keyboard_main
from setup import dp


@dp.message_handler(Command('start'))
async def test(mes: types.Message):
    await mes.answer('Главное меню', reply_markup=inline_keyboard_main)


@dp.message_handler(Command('help'))
async def cmd_help(mes: types.Message):
    await mes.answer("Я помога тебе с учетом рассходов", reply_markup=test_mk)


@dp.message_handler(Command('cancel'))
async def cancel(mes: types.Message):
    await mes.answer('Cancel', reply_markup=types.ReplyKeyboardRemove())

