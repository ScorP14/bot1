from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from handlers.users.user import menu_user_main
from keyboards.callback_data.callback import main_user_callback_data, main_user_sub_alert_mes
from keyboards.in_line_keyboard.menu_user import inline_keyboard_main_user_sub_alert_mes, inline_keyboard_main_user
from setup import dp, bot
from utils.db_api.models.func_model_user import swap_sub
from utils.db_api.models.models import User

from utils.decorators.decorator import identification, not_subscriber, subscriber


@dp.callback_query_handler(main_user_callback_data.filter(key=['Sub_user']))
@identification
@not_subscriber
async def sub_true(query: types.CallbackQuery):
    """
    Проверяет декораторами есть ли пользователь в базе,
    подписан ли он, если НЕТ, вызывает клавиатуру с вопросом на добавление - Да-Нет-Выхолд
    """
    return await bot.edit_message_text('Хотите подписаться?',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=inline_keyboard_main_user_sub_alert_mes)


@dp.callback_query_handler(main_user_callback_data.filter(key=['Del_Sub_user']))
@identification
@subscriber
async def sub_false(query: types.CallbackQuery):
    """
    Проверяет декораторами есть ли пользователь в базе
    подписан ли он, если ДА, вызывает клавиатуру с вопросом на удаление - Да-Нет-Выхолд
    """
    return await bot.edit_message_text('Вы уверены, что хотите отписаться?',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=inline_keyboard_main_user_sub_alert_mes)


@dp.callback_query_handler(main_user_sub_alert_mes.filter(answer=['OK', 'NO']))
async def sub_alert_swap(query: types.CallbackQuery, callback_data: dict):
    """
    Обрабатывает клавиатуру с вопросом на (Да-Нет-Выхолд)
    """
    text_mes = query.message.text.split()[-1].rstrip('?')
    text = 'Вы успешно подписались'
    if text_mes == 'отписаться':
        text = 'Вы успешно отписались'
    if callback_data['answer'] == 'OK':
        swap_sub(query.from_user.id)
        return await bot.edit_message_text(text,
                                           query.from_user.id, query.message.message_id,
                                           reply_markup=inline_keyboard_main_user)
    elif callback_data['answer'] == 'NO':
        return await menu_user_main(query)
            #await bot.edit_message_text(f'Отмена',query.from_user.id, query.message.message_id,reply_markup=inline_keyboard_main_user)
    return await bot.edit_message_text(f'Произошла ошибка в Саб делит Мес',
                                       query.from_user.id, query.message.message_id,
                                       reply_markup=ReplyKeyboardRemove())
