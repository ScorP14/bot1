from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.callback_data.callback import cdb_menu_expenses, cbd_menu
from keyboards.default_button.expense import rasxod
from keyboards.in_line_keyboard.expenses import in_keyboard_main_expenses
from setup import dp, bot
from states.state import StateAddExpenses
from utils.db_api.models.func_model_expenses import add_expenses
from utils.db_api.models.func_model_view_expenses import search_name_expenses_in_db
from utils.db_api.utility_for_db import parse_text_for_expenses


@dp.callback_query_handler(cbd_menu.filter(key='Expenses'))
async def callback_vote_action(query: types.CallbackQuery):

    await query.answer()
    await bot.edit_message_text('Расходы', query.from_user.id, query.message.message_id,

                                reply_markup=in_keyboard_main_expenses
                                )


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Add_exp'))
async def callback_vote_action(query: types.CallbackQuery):

    await query.answer(text='Add_exp')
    await StateAddExpenses.state_category.set()
    await bot.send_message(chat_id=query.message.chat.id,
                           text='Добавляем расход, введите расход',
                           reply_markup=rasxod)


@dp.message_handler(lambda message: message.text != 'Отмена', state=StateAddExpenses.state_category)
async def process_name(mes: types.Message, state: FSMContext):
    if not parse_text_for_expenses(mes.text):
        return await mes.answer(text='Ошибка ввода, попробуйте еще',
                                    reply_markup=rasxod)
    name_exp_str, price = parse_text_for_expenses(mes.text)
    name_exp = search_name_expenses_in_db(name_exp_str)
    if not name_exp:
        return await mes.answer(text='Такого рассхода нету)',
                                reply_markup=rasxod)
    if not add_expenses(mes.from_user.id, name_exp_str, price):
        await state.finish()
        return await mes.answer(text='Ошибка с добавлением расхода',
                                reply_markup=ReplyKeyboardRemove())
    print(f'Ваш запрос - {name_exp_str}, цена {float(price)}')

    await mes.answer(f'Ваш запрос - {name_exp_str}, цена {float(price)}', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(lambda message: message.text == 'Отмена', state=StateAddExpenses.state_category)
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отмена', reply_markup=types.ReplyKeyboardRemove())
