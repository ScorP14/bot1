from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command

import logging

import config
from kb import inline_keyboard_main, test_mk, main_callback_data
from db.main_db import sub_user_true, add_user, del_user, sub_user_false, get_user

from decorators import identification

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


API_TOKEN = config.API_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())










@dp.message_handler(Command('add'))
async def check(mes: types.Message):
    user = add_user(mes.from_user.id, mes.from_user.full_name)
    if user[1]:
        text = f'Пользователь:{mes.from_user.id}-{mes.from_user.full_name} создан'
        return await mes.answer(text)
    await mes.answer('Пользователь уже создан')


@dp.message_handler(Command('del'))
@identification
async def check(mes: types.Message):
    user = del_user(mes.from_user.id)
    if user:
        return await mes.reply('Пользователь удален')


@dp.message_handler(Command('check'))
async def check(mes: types.Message):
    check_user = get_user(mes.from_user.id)
    text = f"""ID-{mes.from_user.id}, User_name-{mes.from_user.full_name}-{mes.date}
В базе: {check_user.name}, подписка: {check_user.sub}"""
    await mes.answer(text)


@dp.message_handler(commands=['help'])
async def cmd_help(mes: types.Message):
    await mes.answer("""
    Я помога тебе с учетом рассходов
    """, reply_markup=test_mk)


@dp.message_handler(commands=['cancel'])
async def cancel(mes: types.Message):
    await mes.answer('Cancel', reply_markup=types.ReplyKeyboardRemove())







@dp.message_handler(Command('test'))
async def test(mes: types.Message):
   await mes.answer('Главное меню', reply_markup=inline_keyboard_main)


@dp.callback_query_handler(main_callback_data.filter(key=['User', 'Category', 'Cancel']))
async def callback_vote_action(query: types.CallbackQuery, callback_data: dict):
    await query.answer()
    await bot.edit_message_text()
    await bot.edit_message_text(
        f'You voted {callback_data}! Now you have vote[s].',
        query.from_user.id,
        query.message.message_id
    )







@dp.message_handler()
async def echo(mes: types.Message):
    await mes.answer(f'Echo -  {mes.text}', reply_markup=types.ReplyKeyboardRemove())




@dp.message_handler(Command('sub_true'))
@identification
async def sub_true(message: types.Message):
    us = sub_user_true(message.from_user.id)
    await message.reply(f'Check - {us}')


@dp.message_handler(Command('sub_false'))
@identification
async def sub_false(message: types.Message):
    us = sub_user_false(message.from_user.id)
    await message.reply(f'Check - {us}')







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
