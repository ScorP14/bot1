import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode

from setup import dp, bot
import aiogram.utils.markdown as md


class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()

@dp.message_handler(commands='qweasd')
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    await Form.name.set()

    await message.reply("Как твое имя?")


# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply("Сколько тебе лет?")


# Check age. Age gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await Form.next()
    await state.update_data(age=int(message.text))

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Male", "Female")
    markup.add("Other")

    await message.reply("What is your gender?", reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
async def process_gender_invalid(message: types.Message):
    """
    In this example gender has to be one of: Male, Female, Other.
    """
    return await message.reply("Bad gender name. Choose your gender from the keyboard.")


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Hi! Nice to meet you,', md.bold(data['name'])),
                md.text('Age:', md.code(data['age'])),
                md.text('Gender:', data['gender']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )




#text=f'Name - {data["name"]}Age - {data["age"]}Gender - {data["gender"]}',reply_markup=markup, parse_mode=ParseMode.MARKDOWN,


    # Finish conversation
    await state.finish()














# @dp.message_handler()
# async def check(mes: types.Message):
#     '''Ехо'''
#     await mes.answer('echp last -' + mes.text)




# @dp.message_handler(commands="set_commands", state="*")
# async def cmd_set_commands(message: types.Message):
#     if message.from_user.id ==321:  # Подставьте сюда свой Telegram ID
#         commands = [types.BotCommand(command="/drinks", description="Заказать напитки"),
#                     types.BotCommand(command="/food", description="Заказать блюда")]
#
#         await bot.set_my_commands([])
#         await message.answer("Команды настроены.")
# Хэндлер на команду /start
# @dp.message_handler(commands=["start111"])
# async def cmd_start(message: types.Message):
#     poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     poll_keyboard.add(types.KeyboardButton(text="Создать викторину",
#                                            request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
#     poll_keyboard.add(types.KeyboardButton(text="Отмена"))
#     await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)
#
#
# # Хэндлер на текстовое сообщение с текстом “Отмена”
# @dp.message_handler(lambda message: message.text == "Отмена")
# async def action_cancel(message: types.Message):
#     remove_keyboard = types.ReplyKeyboardRemove()
#     await message.answer("Действие отменено. Введите /start111, чтобы начать заново.", reply_markup=remove_keyboard)
