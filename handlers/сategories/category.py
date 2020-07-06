from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.callback_data.callback import test_callback_data
from keyboards.default_button.test_menu import test_mk
from keyboards.in_line_keyboard.menu import inline_keyboard_main
from keyboards.in_line_keyboard.menu_user import get_kb_test
from main import dp, bot



@dp.message_handler(Command('check'))
async def check(mes: types.Message):

    await mes.answer('Пук из чек', reply_markup=get_kb_test())


@dp.callback_query_handler(test_callback_data.filter())
async def callback_vote_action(query: types.CallbackQuery, callback_data: dict):
    print(callback_data)
    await query.answer('ok')
    # await bot.edit_message_text(
    #     f'Пук из юзера',
    #     query.from_user.id, query.message.message_id,
    #     reply_markup=inline_keyboard_main_user
    # )

@dp.message_handler(commands=['help'])
async def cmd_help(mes: types.Message):
    await mes.answer("""
    Я помога тебе с учетом рассходов
    """, reply_markup=test_mk)


@dp.message_handler(commands=['cancel'])
async def cancel(mes: types.Message):
    await mes.answer('Cancel', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Command('test'))
async def test(mes: types.Message):
    await mes.answer('Главное меню', reply_markup=inline_keyboard_main)
