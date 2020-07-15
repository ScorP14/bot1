from aiogram import types

from keyboards.callback_data.callback import cdb_menu_expenses
from keyboards.in_line_keyboard.expenses import in_keyboard_main_expenses
from setup import dp, bot
from utils.db_api.models.func_model_expenses import view_expenses



@dp.callback_query_handler(cdb_menu_expenses.filter(key='View_exp'))
async def callback_vote_action(query: types.CallbackQuery):
    select = view_expenses(query.from_user.id)
    text = ''
    temp = 0
    for i in select:
        text += f'{i.view_expense.category}: {i.view_expense.name_expense} - {i.price}\n'
        temp += i.price

    await query.answer()
    await bot.edit_message_text(text + str(temp), query.from_user.id, query.message.message_id,

                                reply_markup=in_keyboard_main_expenses
                                )


'''
def view_expenses(id_tg: int, main=False):
user = get_user(id_tg)
epens = Expenses.select().where(Expenses.user == user)
if main:
    epens = Expenses.select().where((Expenses.user == user)& (Expenses.main_expense >> main))
for i in epens:
    yield i
    '''