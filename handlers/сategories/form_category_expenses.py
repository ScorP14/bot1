from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.сategories.category import menu_category
from keyboards.callback_data.callback import cdb_menu_category, cdb_menu_exp_from_category_paginate
from keyboards.in_line_keyboard.categories import get_kb_expenses_from_category, test12312
from setup import bot, dp
from states.state import PaginatorForExpenses
from utils.db_api.models.func_model_categories import get_list_categories
from utils.db_api.models.func_model_view_expenses import get_name_expenses_from_category
from utils.paginate.paginate_exp_from_category import Paginator


@dp.callback_query_handler(cdb_menu_category.filter(key=get_list_categories()))
async def callback_vote_action(query: types.CallbackQuery, callback_data: dict):

    await PaginatorForExpenses.St1.set()
    PaginatorForExpenses.paginator = Paginator(get_name_expenses_from_category(callback_data['key']), 4)
    PaginatorForExpenses.page = PaginatorForExpenses.paginator.page(1)
    await bot.edit_message_text(
        f'Data - {callback_data}',
        query.from_user.id,
        query.message.message_id, reply_markup=test12312(PaginatorForExpenses.page.object_list))


@dp.callback_query_handler(cdb_menu_exp_from_category_paginate.filter(
    key=['Expenses_paginator_back', 'Expenses_paginator_next']), state=PaginatorForExpenses.St1)
async def cmd_s123tart(query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    if callback_data['key'] == 'Expenses_paginator_back':
        if PaginatorForExpenses.page.has_previous():
            PaginatorForExpenses.page = PaginatorForExpenses.paginator.page(PaginatorForExpenses.page.previous_page_number())
        else:
            PaginatorForExpenses.page = PaginatorForExpenses.paginator.page(1)
    if callback_data['key'] == 'Expenses_paginator_next':
        if PaginatorForExpenses.page.has_next():
            PaginatorForExpenses.page = PaginatorForExpenses.paginator.page(PaginatorForExpenses.page.next_page_number())
        else:
            PaginatorForExpenses.page = PaginatorForExpenses.paginator.page(1)
    text = f'{str(PaginatorForExpenses.page.number)} из {str(PaginatorForExpenses.paginator.num_pages())}'
    await bot.edit_message_text(text=f'Data - {callback_data}\n Страница - {text}',
                                chat_id=query.message.chat.id, message_id=query.message.message_id,
                                reply_markup=test12312(PaginatorForExpenses.page.object_list)
                                )




@dp.callback_query_handler(cdb_menu_category.filter(key='Back_exp'))
async def menu_category_exp_back(query: types.CallbackQuery):
    return await menu_category(query)
