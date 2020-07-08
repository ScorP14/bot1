from aiogram import types
from keyboards.callback_data.callback import main_expenses_callback_data, main_callback_data
from keyboards.in_line_keyboard.categories import get_kb_categories
from main import dp, bot



@dp.callback_query_handler(main_callback_data.filter(key='Expenses'))
async def callback_vote_action(query: types.CallbackQuery):

    await query.answer(text='Тест QWE')
    await bot.edit_message_text('Оки', query.from_user.id, query.message.message_id,
                                reply_markup=get_kb_categories())


@dp.callback_query_handler(main_expenses_callback_data.filter())
async def callback_vote_action(query: types.CallbackQuery):
    print(query.data)
    await query.answer()







