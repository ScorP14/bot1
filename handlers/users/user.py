from aiogram import types

from keyboards.callback_data.callback import main_callback_data, main_user_callback_data
from keyboards.in_line_keyboard.menu_user import inline_keyboard_main_user
from main import dp, bot
from utils.db_api.main_db import add_user, del_user
from utils.decorators.decorator import not_identification, identification


@dp.callback_query_handler(main_callback_data.filter(key=['User']))
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f'Здравсвуй {query.from_user.full_name}',
        query.from_user.id, query.message.message_id,
        reply_markup=inline_keyboard_main_user
    )


@dp.callback_query_handler(main_user_callback_data.filter(key='Add_user'))
@not_identification
async def callback_vote_action(query: types.CallbackQuery):
    users = add_user(query.from_user.id, query.from_user.full_name)
    if users[1]:
        text = f'Пользователь:{query.from_user.id}-{query.from_user.full_name} создан'
        await query.answer(text)
        return await bot.edit_message_text(text, query.from_user.id, query.message.message_id,
                                           reply_markup=inline_keyboard_main_user)
    await query.answer('Пользователь уже создан')
    await bot.edit_message_text(
        'Пользователь уже создан',
        query.from_user.id, query.message.message_id,
        reply_markup=inline_keyboard_main_user)


@dp.callback_query_handler(main_user_callback_data.filter(key=['Del_user']))
@identification
async def callback_vote_action(query: types.CallbackQuery):
    await query.answer()
    users = del_user(query.from_user.id)
    if users:
        return await bot.edit_message_text('Пользователь удален',
                                           query.from_user.id, query.message.message_id,
                                           reply_markup=inline_keyboard_main_user)
    return await bot.edit_message_text('Произошла ошибка', query.from_user.id, query.message.message_id)


@dp.callback_query_handler(text='Cancel')
async def echo(query: types.CallbackQuery):
    await bot.edit_message_text(
        f'Echo cancel',
        query.from_user.id,
        query.message.message_id
    )
