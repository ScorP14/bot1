from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.callback_data.callback import main_expenses_callback_data, main_callback_data
from keyboards.default_button.expense import rasxod
from keyboards.in_line_keyboard.expenses import inline_keyboard_main_category, in_keyboard_main_expenses
from setup import dp, bot
from states.state import StateAddExpenses
from utils.db_api.utility_for_db import parse_text_for_expenses


@dp.callback_query_handler(main_callback_data.filter(key='Expenses'))
async def callback_vote_action(query: types.CallbackQuery):

    await query.answer()
    await bot.edit_message_text('Расходы', query.from_user.id, query.message.message_id,

                                reply_markup=in_keyboard_main_expenses
                                )


@dp.callback_query_handler(main_expenses_callback_data.filter(id='Add_exp'))
async def callback_vote_action(query: types.CallbackQuery):

    await query.answer(text='Add_exp')
    await StateAddExpenses.state_category.set()
    await bot.send_message(chat_id=query.message.chat.id,
                           text='Добавляем расход, введите расход',
                           reply_markup=rasxod)






@dp.message_handler(lambda message: message.text != 'Отмена', state=StateAddExpenses.state_category)
async def process_name(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        return await cancel_handler()
    if not parse_text_for_expenses(message.text):
        return await message.answer(text='Ошибка ввода, попробуйте еще',
                                    reply_markup=rasxod)

    cat, price = parse_text_for_expenses(message.text)

    print(f'Ваш запрос - {cat}, цена {float(price)}')

    # await StateAddExpenses.state_price.set()
    await message.answer(f'Ваш запрос - {cat}, цена {float(price)}', reply_markup=ReplyKeyboardRemove())
    await state.finish()






# @dp.message_handler(state=StateAddExpenses.state_price)
# async def process_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['price'] = message.text
#         print(f'Ваш запрос - {data["category"]}, цена {data["price"]}')
#         await message.answer(f'Ваш запрос - {data["category"]}, цена {data["price"]}',
#                             reply_markup=types.ReplyKeyboardRemove())
#     await state.finish()





@dp.message_handler(lambda message: message.text == 'Отмена', state=StateAddExpenses.state_category)
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отмена', reply_markup=types.ReplyKeyboardRemove())





