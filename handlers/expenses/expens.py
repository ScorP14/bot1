from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.callback_data.callback import cbd_menu
from keyboards.in_line_keyboard.expenses import in_keyboard_main_expenses
from setup import dp, bot


@dp.callback_query_handler(cbd_menu.filter(key='Expenses'))
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text('Расходы', query.from_user.id, query.message.message_id,

                                reply_markup=in_keyboard_main_expenses
                                )


# @dp.message_handler(state=StateAddExpenses.state_price)
# async def process_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['price'] = message.text
#         print(f'Ваш запрос - {data["category"]}, цена {data["price"]}')
#         await message.answer(f'Ваш запрос - {data["category"]}, цена {data["price"]}',
#                             reply_markup=types.ReplyKeyboardRemove())
#     await state.finish()
