from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.callback_data.callback import cdb_menu_expenses
from keyboards.default_button.expense import rasxod, message_y_n
from keyboards.in_line_keyboard.expenses import in_keyboard_main_expenses, in_keyboard_main_expenses_add_exp
from setup import dp, bot
from states.state import StateAddExpenses, StateAddExpensesCheque
from utils.db_api.models.func_model_expenses import add_expenses
from utils.db_api.models.func_model_view_expenses import search_name_expenses_in_db
from utils.db_api.utility_for_db import parse_text_for_expenses


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Add_exp'))
async def menu_expense_add(query: types.CallbackQuery):
    await query.answer(text='Add_exp')
    await StateAddExpenses.state_category.set()
    await bot.send_message(chat_id=query.message.chat.id,
                           text='Добавляем расход, введите расход',
                           reply_markup=rasxod)


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Add_exp_cheque'))
async def menu_expense_add(query: types.CallbackQuery):
    await query.answer(text='Add_exp')
    await StateAddExpensesCheque.state_category.set()
    await bot.send_message(chat_id=query.message.chat.id,
                           text='Добавляем чек',
                           reply_markup=rasxod)


@dp.message_handler(lambda message: message.text != 'Отмена', state=StateAddExpensesCheque.state_category)
async def process_name(mes: types.Message, state: FSMContext):
    masiv = mes.text.split('\n')

    for i in masiv:
        if not parse_text_for_expenses(i):
            return await mes.answer('Что то не то')
    res = '\n'.join([i for i in masiv])
    async with state.proxy() as data:
        data['items'] = res
    await StateAddExpensesCheque.state_message.set()
    await mes.answer('Вы хотите добавить данный чек?\n' + res, reply_markup=message_y_n)


@dp.message_handler(state=StateAddExpensesCheque.state_message)
async def process_name(mes: types.Message, state: FSMContext):
    text = mes.text
    if text == 'Да':
        await mes.answer('Продукты добавлены')
    if text == 'Отмена':
        await mes.answer('Ну и хуй с тобой ...')
    await state.finish()


@dp.message_handler(lambda message: message.text != 'Отмена', state=StateAddExpenses.state_category)
async def process_name(mes: types.Message, state: FSMContext):
    print(mes.text)

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


@dp.message_handler(lambda message: message.text == 'Отмена', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Добавляем расход', reply_markup=in_keyboard_main_expenses_add_exp, parse_mode='HTML')


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Back_from_add'))
async def menu_category_back(query: types.CallbackQuery):
    await bot.edit_message_text('Расходы', query.from_user.id, query.message.message_id,
                                reply_markup=in_keyboard_main_expenses
                                )
