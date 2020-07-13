from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from setup import dp, bot
from utils.db_api.models.models import Categories
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=
[
    [
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='2', callback_data='2'),
        InlineKeyboardButton(text='3', callback_data='3')
    ],
    [
        InlineKeyboardButton(text='Back', callback_data='Back'),
        InlineKeyboardButton(text='Next', callback_data='Next')
    ],
    [
        InlineKeyboardButton(text='Exit', callback_data='Exit')
    ]
])


class QWE(StatesGroup):
    page = 1
    St1 = State()
    St2 = State()


@dp.message_handler(commands='qweasdzxc')
async def cmd_start(message: types.Message):
    await QWE.St1.set()
    await message.reply("Как твое имя?asdasdasd", reply_markup=kb)


@dp.callback_query_handler(lambda query: query.data in ['1', '2', '3', 'Back', 'Next', 'Exit'], state=QWE.St1)
async def cmd_s123tart(query: types.CallbackQuery, state: FSMContext):
    if query.data == 'Next':
        QWE.page += 1
    if query.data == 'Back':
        if QWE.page > 1:
            QWE.page -= 1
        else:
            await query.answer('Левее пусто)')
    if query.data == 'Exit':
        await state.finish()
        return await bot.edit_message_text(chat_id=query.message.chat.id,
                                           message_id=query.message.message_id,
                                           text='Выход')
    us = Categories.select().limit(10).paginate(QWE.page, 3)

    text = [str(i) for i in us]
    print(QWE.page, text)
    await query.answer('Пук')
    await bot.edit_message_text(chat_id=query.message.chat.id,
                                message_id=query.message.message_id,
                                text=',\n'.join(text),
                                reply_markup=kb)
