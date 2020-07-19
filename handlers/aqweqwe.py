from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.in_line_keyboard.categories import get_kb_expenses_from_category
from setup import dp, bot
from utils.db_api.models.func_model_view_expenses import get_count_expenses_for_paginator
from utils.db_api.models.models import Categories
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class QWE(StatesGroup):
    page = 1
    page_count = None
    St1 = State()
    St2 = State()


# @dp.message_handler(commands='Page')
# async def cmd_start(message: types.Message):
#     await QWE.St1.set()
#     QWE.page_count = get_count_expenses_for_paginator('Продукты')
#     await message.reply("get_kb_expenses_from_category", reply_markup=get_kb_expenses_from_category('Продукты'))


# @dp.callback_query_handler(lambda query: query.data in
#                                          ['Expenses_paginator_back', 'Expenses_paginator_next'], state=QWE.St1)
# async def cmd_s123tart(query: types.CallbackQuery, state: FSMContext):
#     if query.data == 'Next':
#         QWE.page += 1
#     if query.data == 'Back':
#         if QWE.page > 1:
#             QWE.page -= 1
#         else:
#             await query.answer('Левее пусто)')
#     if query.data == 'Exit':
#         await state.finish()
#         return await bot.edit_message_text(chat_id=query.message.chat.id,
#                                            message_id=query.message.message_id,
#                                            text='Выход')
#
#     await query.answer('Пук')
#     await bot.edit_message_text(chat_id=query.message.chat.id,
#                                 message_id=query.message.message_id,
#                                 text=',\n'.join(text),
#                                 reply_markup=kb)
#
#
# @dp.callback_query_handler(lambda query: query.data in ['Exit', ], state='*')
# async def cmd_s123tart(query: types.CallbackQuery, state: FSMContext):
#     print(query.data)
#     await state.finish()
#     await query.answer('Пук')
