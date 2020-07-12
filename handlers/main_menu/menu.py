from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.in_line_keyboard.menu import in_kb_main
from setup import dp


@dp.message_handler(Command('start'))
async def cmd_start(mes: types.Message):
    await mes.answer('Главное меню', reply_markup=in_kb_main)


@dp.message_handler(Command('help'))
async def cmd_help(mes: types.Message):
    await mes.answer("Я помога тебе с учетом рассходов")


@dp.message_handler(Command('cancel'))
async def cmd_cancel(mes: types.Message):
    await mes.answer('Cancel', reply_markup=types.ReplyKeyboardRemove())

