from aiogram import types
from keyboards.callback_data.callback import cbd_menu, cdb_menu_user
from keyboards.in_line_keyboard.menu import in_kb_main
from keyboards.in_line_keyboard.menu_user import in_kb_main_user
from setup import dp, bot
from utils.db_api.models.func_model_user import check_for_user_sub, add_user, del_user

from utils.decorators.decorator import not_identification, identification


@dp.callback_query_handler(cbd_menu.filter(key=['User']))
async def menu_user(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f"""Здравствуй - {query.from_user.full_name}
Подписка - {'Есть' if check_for_user_sub(query.from_user.id) else 'Нету'}
Привествую)
""",
        query.from_user.id, query.message.message_id,
        reply_markup=in_kb_main_user
    )


@dp.callback_query_handler(cdb_menu_user.filter(key='Add_user'))
@not_identification
async def menu_user_add(query: types.CallbackQuery):
    add_user(query.from_user.id, query.from_user.full_name)
    text = f"""Здравствуй - {query.from_user.full_name}
Подписка - {'Есть' if check_for_user_sub(query.from_user.id) else 'Нету'}
Привествую)
"""
    await query.answer(text)
    return await bot.edit_message_text(text,
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=in_kb_main_user)


@dp.callback_query_handler(cdb_menu_user.filter(key=['Del_user']))
@identification
async def menu_user_del(query: types.CallbackQuery):
    await query.answer()
    users = del_user(query.from_user.id)
    if users:
        return await bot.edit_message_text('Пользователь удален',
                                           query.from_user.id, query.message.message_id,
                                           reply_markup=in_kb_main_user)


@dp.callback_query_handler(cdb_menu_user.filter(key=['Back']))
@identification
async def menu_user_back(query: types.CallbackQuery):
    return await bot.edit_message_text('Главное меню', query.from_user.id, query.message.message_id,
                                       reply_markup=in_kb_main)


@dp.callback_query_handler(cdb_menu_user.filter(key=['Exit']))
@identification
async def menu_user_exit(query: types.CallbackQuery):
    return await bot.edit_message_text('Досвидание :)', query.from_user.id, query.message.message_id)