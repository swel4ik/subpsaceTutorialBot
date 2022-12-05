from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.fsm.context import FSMContext
from messages import BotMessages
from keyboards import BotKeyboards
from utils import BotStates

bot_messages = BotMessages()
bot_keyboard = BotKeyboards()
router = Router()  # [1]


@router.message(commands=["start"])
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("What you are interested in?", reply_markup=bot_keyboard.get_main_kb())
    await state.set_state(BotStates.main_menu)
    await state.update_data(menu='main')


@router.message(commands=["problem"])
async def with_puree(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.user_problem)
    bot_mes = "Try to reproduce your problem in text (use general words from logs or error):"
    await message.reply(bot_mes, reply_markup=ReplyKeyboardRemove())


@router.message()
async def echo_message(msg: types.Message, ):
    text = '''
Current supported testnet: Gemini 3
Write /start for installation tutorial
Write /problem to describe your issue 
        '''
    await msg.answer(text)


@router.callback_query(text="cancel")
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Ok, see you next time",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()
    await callback.answer()


@router.callback_query(text="installation_type_menu")
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Choose installation type", reply_markup=bot_keyboard.get_installation_kb())
    await state.set_state(BotStates.choosing_installation_type)
    await state.update_data(menu='installation_type')
    await callback.answer()


@router.callback_query(text="req")
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.req_info)
    await callback.message.answer("CPU: 2 Core+\nRAM: 4GB+(Rec. 8GB)\nStorage: 150 GB")
    await callback.answer()


# @router.message(Text(text='Back ◀️'))
# async def with_puree(message: types.Message, state: FSMContext):
#     curr_state = await state.get_data()
#     if curr_state['menu'] == 'installation_type':
#         keyboard = types.ReplyKeyboardMarkup(
#             keyboard=bot_keyboard.start_kb,
#             resize_keyboard=True,
#             input_field_placeholder="Choose"
#         )
#         await message.answer("What you are interested in?", reply_markup=keyboard)
#         await state.set_state(BotStates.main_menu)
#         await state.update_data(menu='main')
#
#     elif curr_state['menu'] == 'installation_step':
#         keyboard = types.ReplyKeyboardMarkup(
#             keyboard=bot_keyboard.docker_steps_kb,
#             resize_keyboard=True,
#             input_field_placeholder="Choose installation step"
#         )
#         await message.answer("Choose installation step", reply_markup=keyboard)
#         await state.update_data(menu='installation_step')
#
#     elif curr_state['menu'] == 'logs_example':
#         keyboard = types.ReplyKeyboardMarkup(
#             keyboard=bot_keyboard.docker_steps_kb,
#             resize_keyboard=True,
#             input_field_placeholder="Choose installation step"
#         )
#         await message.answer("Choose installation step", reply_markup=keyboard)
#         await state.update_data(menu='installation_step')
