from aiogram import Router
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.fsm.context import FSMContext
from messages import BotMessages
from keyboards import BotKeyboards
from utils import BotStates, InstallIssues

bot_messages = BotMessages()
bot_keyboard = BotKeyboards()
issues = InstallIssues()
router = Router()  # [1]


@router.message(commands=["start"])
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("What you are interested in?", reply_markup=bot_keyboard.get_main_kb())
    await state.set_state(BotStates.main_menu)
    await state.update_data(menu='main')


@router.message(commands=["problem"])
async def with_puree(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.user_problem)
    bot_mes = "Try to reproduce your problem in text (use the error string from logs or error):"
    await message.reply(bot_mes, reply_markup=ReplyKeyboardRemove())


@router.message(commands=["language"])
async def with_puree(message: types.Message, state: FSMContext):
    # await state.set_state(BotStates.user_problem)
    bot_mes = "Pic the language:"
    await message.reply(bot_mes, reply_markup=ReplyKeyboardRemove())


@router.message(state=BotStates.user_problem)
async def problem_state(message: types.Message):
    problem_text = message.text.lower()

    if 'is invalid because' in problem_text or 'it should be an array' in problem_text:
        await message.reply(issues.docker_invalid_type)

    elif 'space left' in problem_text:
        await message.reply('Your disk space are full. Try to add more space on your disk.')

    elif 'submitting a transaction' in problem_text or 'pool error' in problem_text:
        await message.reply(issues.submitting_tx)

    elif 'while dialing' in problem_text:
        await message.reply(issues.error_while_dialing)

    elif 'bootnode you want' in problem_text:
        await message.reply(issues.bootnode_not_connected)

    elif 'stuck' in problem_text:
        await message.reply(issues.farmer_stucked)

    elif 'is unhealthy' in problem_text:
        await message.reply(issues.node_is_unhealthy)

    elif 'inherents failed' in problem_text or 'incorrectrootblocksList' in problem_text or 'verification failed' in problem_text:
        await message.reply(issues.consensus_error_import_failed)

    elif 'error importing block' in problem_text or 'err(unknownparent)' in problem_text:
        await message.reply(issues.error_importing_block)

    elif 'error response from daemon' in problem_text or 'userland proxy' in problem_text:
        await message.reply(issues.error_starting_userland_proxy)

    elif 'chain_constants' in problem_text or 'exported method subspace' in problem_text:
        await message.reply(issues.exported_method_subspaceapi_chain_constants)

    elif 'error with block built' in problem_text or 'transaction pool error' in problem_text or 'invalid transaction validity' in problem_text:
        await message.reply(issues.invalid_transaction_validity)

    elif 'failed to allocate' in problem_text or 'cannot allocate' in problem_text or 'os error 12' in problem_text:
        await message.reply(issues.cannot_allocate_memory)

    else:
        await message.reply("Hmm, seems like I haven't met this problem earlier 🧐. "
                            "Try to rephrase your error or find the answer by your hand here: "
                            "https://forum.subspace.network/")

@router.message()
async def echo_message(msg: types.Message, state: FSMContext):
    # cur_state = state.get_state()
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
