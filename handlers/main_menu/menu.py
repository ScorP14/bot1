from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from keyboards.callback_data.callback import cbd_menu
from keyboards.in_line_keyboard.menu import in_kb_main
from setup import dp, bot


@dp.message_handler(Command('start'))
async def cmd_start(mes: types.Message):
    await mes.answer('Главное меню', reply_markup=in_kb_main)


@dp.message_handler(Command('help'))
async def cmd_help(mes: types.Message):
    await mes.answer("Я помога тебе с учетом рассходов")


@dp.message_handler(Command('clear'))
async def cmd_help(mes: types.Message):
    
    await mes.answer("Очистил", reply_markup=ReplyKeyboardRemove())




@dp.callback_query_handler(cbd_menu.filter(key='Cancel'))
async def cmd_cancel(query: types.CallbackQuery):
    return await bot.edit_message_text('Досвидание :)', query.from_user.id, query.message.message_id,)

