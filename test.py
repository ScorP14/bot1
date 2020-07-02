from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Command

import logging
import config
import kb
from db.main_db import sub_user_true, check_for_user, add_user, del_user, sub_user_false
from utility import identification, subscriber

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger()






API_TOKEN = config.API_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(Command('check'))
async def check(message: types.Message):
    check = check_for_user(message.from_user.id)
    loger.info(f'Из фун - {check}')
    await message.reply(f'Check - {check}')


@dp.message_handler(Command('add'))
async def check(message: types.Message):
    check = check_for_user(message.from_user.id)
    if not check:
        add_user(message.from_user.id, message.from_user.full_name)
        text = f'Пользователь:{message.from_user.id}-{message.from_user.full_name} добавлен'
        return await message.reply(text)
    text = 'Пользователь уже есть'
    await message.reply(text)


@dp.message_handler(Command('del'))
async def check(message: types.Message):
    check = check_for_user(message.from_user.id)
    if check:
        del_user(message.from_user.id)
        text = f'Пользователь:{message.from_user.id}-{message.from_user.full_name} удален'
        return await message.reply(text)
    text = 'Пользовтель уже удален или его нет'
    return await message.reply(text)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply(f'Vote! You have votes now.',)


@dp.message_handler(Command('subt'))
@identification
async def sub_true(message: types.Message):
    us = sub_user_true(message.from_user.id)
    await message.reply(f'Check - {us}')


@dp.message_handler(Command('subf'))
@identification
async def sub_false(message: types.Message):
    us = sub_user_false(message.from_user.id)
    await message.reply(f'Check - {us}')


@dp.message_handler(commands=['help'])
@identification
async def cmd_start(message: types.Message):
    await message.reply("""
    /check
    /add
    /del
    /subt
    /subf
    /qwe
    """, reply_markup=kb.test_mk)


@dp.message_handler(commands=['qwe'])
async def cmd_start(message: types.Message):
    await message.reply(f'All qwe  {message.text}', reply_markup=kb.get_keyboard(message.from_user.id))


@dp.message_handler()
async def cmd_start(message: types.Message):
    await message.reply(f'All {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
