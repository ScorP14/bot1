from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Command

import logging

import config
import kb
from db.main_db import sub_user_true, check_for_user, add_user, del_user, sub_user_false, get_user

from utility import identification

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


API_TOKEN = config.API_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
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
    """, reply_markup=kb.test_mk)


@dp.message_handler(commands=['cancel'])
async def cancel(mes: types.Message):
    await mes.answer('Cancel', reply_markup=types.ReplyKeyboardRemove())


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
