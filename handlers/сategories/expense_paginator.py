import math

from aiogram import types

from keyboards.callback_data.callback import cdb_menu_exp_from_category_paginate
from keyboards.in_line_keyboard.categories import get_kb_expenses_from_category
from setup import dp, bot
from utils.db_api.models.func_model_view_expenses import get_count_expenses_for_paginator, \
    get_name_expenses_from_category_paginator, get_name_expenses_from_category
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

'''

@dp.message_handler(commands='Page')
async def cmd_start(message: types.Message):
    await CategoryPaginateState.St1.set()
    CategoryPaginateState.paginate = Paginator(get_name_expenses_from_category('Продукты'), 1, 4)
    await message.reply("get_kb_expenses_from_category", reply_markup=get_kb_expenses_from_category('Продукты'))


@dp.callback_query_handler(cdb_menu_exp_from_category_paginate.filter(
    key=['Expenses_paginator_back', 'Expenses_paginator_next']), state=Paginate.St1)
async def cmd_s123tart(query: types.CallbackQuery, state: FSMContext):
    print(state.proxy().items())
    if query.data == 'Expenses_paginator_back':
        if Paginate_state.page < Paginate_state.page_count:
            Paginate_state.page += 1
        else:
            return await query.answer('Право пусто)')
    if query.data == 'Expenses_paginator_next':
        if Paginate_state.page > 1:
            Paginate_state.page -= 1
        else:
            return await query.answer('Левее пусто)')
    await query.answer('Пук')
    # : {Paginate.page}-{Paginate.pages}-{Paginate.page_count}
    await bot.edit_message_text(text=f'{query.data}',
                                chat_id=query.message.chat.id, message_id=query.message.message_id,
                                reply_markup=get_name_expenses_from_category_paginator(
                                    Paginate_state.category, Paginate_state.page, Paginate_state.pages)
                                )


@dp.callback_query_handler(cdb_menu_exp_from_category_paginate.filter(key='Exit'), state='*')
async def cmd_s123tart(query: types.CallbackQuery, state: FSMContext):
    print(query.data)
    await state.finish()
    await query.answer('Пук')'''