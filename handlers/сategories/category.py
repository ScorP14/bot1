from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.callback_data.callback import main_callback_data, main_category_callback_data
from keyboards.in_line_keyboard.categories import get_kb_categories
from keyboards.in_line_keyboard.menu_user import get_kb_test
from main import dp, bot
from utils.db_api.models.categories import Categories
from utils.decorators.decorator import test_decor


@dp.callback_query_handler(main_callback_data.filter(key='Category'))
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f'Категории',
        query.from_user.id,
        query.message.message_id, reply_markup=get_kb_categories()
    )


@dp.callback_query_handler(main_category_callback_data.filter(key= Categories.get_list_categories()))
@test_decor
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f'asd {query.data}',
        query.from_user.id,
        query.message.message_id, reply_markup=get_kb_categories())












@dp.message_handler(Command('check'))
async def check(mes: types.Message):

    await mes.answer('Пук из чек', reply_markup=get_kb_test())




