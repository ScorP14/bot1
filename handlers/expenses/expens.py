from aiogram import types

from keyboards.callback_data.callback import cbd_menu, cdb_menu_expenses
from keyboards.in_line_keyboard.expenses import in_keyboard_main_expenses, in_keyboard_main_expenses_add_exp
from keyboards.in_line_keyboard.menu import in_kb_main
from setup import dp, bot


@dp.callback_query_handler(cbd_menu.filter(key='Expenses'))
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text('Расходы', query.from_user.id, query.message.message_id,
                                reply_markup=in_keyboard_main_expenses
                                )


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Add_exp_menu'))
async def menu_expense_add(query: types.CallbackQuery):
    await bot.edit_message_text('Добавляем расход',
                                query.from_user.id, query.message.message_id,
                                reply_markup=in_keyboard_main_expenses_add_exp)


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Back'))
async def menu_category_back(query: types.CallbackQuery):
    await query.bot.edit_message_text('Главное меню', query.from_user.id, query.message.message_id,
                                      reply_markup=in_kb_main)


@dp.callback_query_handler(cdb_menu_expenses.filter(key='Exit'))
async def menu_category_exit(query: types.CallbackQuery):
    return await bot.edit_message_text('Досвидание :)',
                                       query.from_user.id, query.message.message_id)

# @dp.message_handler(state=StateAddExpenses.state_price)
# async def process_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['price'] = message.text
#         print(f'Ваш запрос - {data["category"]}, цена {data["price"]}')
#         await message.answer(f'Ваш запрос - {data["category"]}, цена {data["price"]}',
#                             reply_markup=types.ReplyKeyboardRemove())
#     await state.finish()
