from aiogram import types

from handlers.сategories.category import menu_category
from keyboards.callback_data.callback import cdb_menu_category
from keyboards.in_line_keyboard.categories import get_kb_expenses_from_category
from setup import bot, dp
from utils.db_api.models.func_model_categories import get_list_categories


@dp.callback_query_handler(cdb_menu_category.filter(key=get_list_categories()))
async def callback_vote_action(query: types.CallbackQuery, callback_data: dict):
    await bot.edit_message_text(
        f'Data - {query.data}',
        query.from_user.id,
        query.message.message_id, reply_markup=get_kb_expenses_from_category(callback_data['key']))


@dp.callback_query_handler(cdb_menu_category.filter(key='Back_exp'))
async def menu_category_exp_back(query: types.CallbackQuery):
    return await menu_category(query)
