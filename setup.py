import logging

from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

likes = {}

test_cb = CallbackData('post', 'action')

kb = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('OK', callback_data=test_cb.new(action='OK')),
    types.InlineKeyboardButton('NO', callback_data=test_cb.new(action='NO'))
)




@dp.message_handler(commands=['start'])
async def test_func(message: types.Message):
    like_an = likes.get(message.from_user.id, 0)
    print(likes)
    await message.reply(f'Vote! You have {like_an} votes now.', reply_markup=kb)


@dp.callback_query_handler(test_cb.filter(action=['OK', 'NO']))
async def callback_vote_action(query: types.CallbackQuery, callback_data: dict):
    print(callback_data)
    print(query)
    await query.answer()
    callback_data_action = callback_data['action']
    print(callback_data_action)
    likes_count = likes.get(query.from_user.id, 0)

    if callback_data_action == 'OK':
        likes_count += 1
    else:
        likes_count -= 1

    likes[query.from_user.id] = likes_count  # update amount of likes in storage

    await bot.edit_message_text(
        f'You voted {callback_data_action}! Now you have {likes_count} vote[s].',
        query.from_user.id,
        query.message.message_id,
        reply_markup=kb,
    )



@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    msg = '''
    Это комагда хелп
    '''
    await message.reply(msg)


@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)