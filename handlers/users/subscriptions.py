from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from handlers.users.user import menu_user
from keyboards.callback_data.callback import cdb_menu_user, cdb_user_sub_alert_mes, cdb_menu_user_sub
from keyboards.in_line_keyboard.menu_user import in_kb_sub_alert_mes, in_kb_user_sub

from setup import dp, bot
from utils.db_api.models.func_model_user import swap_sub, check_for_user_sub

from utils.decorators.decorator import identification, not_subscriber, subscriber


@dp.callback_query_handler(cdb_menu_user.filter(key=['Sub_user']))
async def sub_menu(query: types.CallbackQuery):
    """
    Проверяет декораторами есть ли пользователь в базе,
    подписан ли он, если НЕТ, вызывает клавиатуру с вопросом на добавление - Да-Нет-Выхолд
    """
    return await bot.edit_message_text('Вы подписаны :)'
                                       if check_for_user_sub(query.from_user.id) else 'Вы не подписаны :(',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=in_kb_user_sub)


@dp.callback_query_handler(cdb_menu_user_sub.filter(key=['User_sub_true']))
@identification
@not_subscriber
async def sub_true(query: types.CallbackQuery):
    """
    Проверяет декораторами есть ли пользователь в базе,
    подписан ли он, если НЕТ, вызывает клавиатуру с вопросом на добавление - Да-Нет-Выхолд
    """
    return await bot.edit_message_text('Хотите подписаться?',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=in_kb_sub_alert_mes)


@dp.callback_query_handler(cdb_menu_user_sub.filter(key=['User_sub_false']))
@identification
@subscriber
async def sub_false(query: types.CallbackQuery):
    """
    Проверяет декораторами есть ли пользователь в базе
    подписан ли он, если ДА, вызывает клавиатуру с вопросом на удаление - Да-Нет-Выхолд
    """
    return await bot.edit_message_text('Вы уверены, что хотите отписаться?',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=in_kb_sub_alert_mes)


@dp.callback_query_handler(cdb_menu_user_sub.filter(key=['Cancel']))
async def back(query: types.CallbackQuery):
    return await menu_user(query)


@dp.callback_query_handler(cdb_user_sub_alert_mes.filter(answer=['OK', 'NO', 'Cancel']))
async def sub_alert_swap(query: types.CallbackQuery, callback_data: dict):
    """
    Обрабатывает клавиатуру с вопросом на (Да-Нет-Выхолд)
    """
    text_mes = query.message.text.split()[-1].rstrip('?')
    text = 'Вы успешно отписались' if text_mes == 'отписаться' else 'Вы успешно подписались'
    if callback_data['answer'] == 'OK':
        swap_sub(query.from_user.id)
        await query.answer(text)
        return await sub_menu(query)
    elif callback_data['answer'] == 'NO' or callback_data['answer'] == 'Cancel':
        await query.answer('Отмена :)')
        return await sub_menu(query)

    return await bot.edit_message_text(f'Произошла ошибка в Саб делит Мес',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=ReplyKeyboardRemove())
