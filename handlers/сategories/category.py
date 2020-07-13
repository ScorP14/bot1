from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.callback_data.callback import cbd_menu, cdb_menu_category
from keyboards.in_line_keyboard.categories import get_kb_categories
from setup import dp, bot
from utils.db_api.models.func_model_categories import get_list_categories


@dp.callback_query_handler(cbd_menu.filter(key='Category'))
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f'Категории',
        query.from_user.id,
        query.message.message_id, reply_markup=get_kb_categories()
    )


@dp.callback_query_handler(cdb_menu_category.filter(key=get_list_categories()))
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f'Data - {query.data}',
        query.from_user.id,
        query.message.message_id, reply_markup=get_kb_categories())






