from aiogram import Router
from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext
from messages import BotMessages
from keyboards import BotKeyboards
from aiogram.types import FSInputFile
from aiogram.methods.send_photo import SendPhoto

bot_messages = BotMessages()
bot_keyboard = BotKeyboards()
router = Router()


@router.callback_query(text="docker_0")
async def docker_step_0(callback: types.CallbackQuery, state: FSMContext):
    wallet_img = FSInputFile('media/wallet_ex.png')
    await callback.message.answer(bot_messages.docker_messages['Step_0_0'], parse_mode="Markdown")
    await callback.message.answer(bot_messages.docker_messages['Step_0_1'], parse_mode="Markdown")
    await SendPhoto(chat_id=callback.message.chat.id, photo=wallet_img)
    await callback.message.answer(".", reply_markup=bot_keyboard.get_docker_installation_kb())
    await callback.answer()


@router.callback_query(text="docker_1")
async def docker_step_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_messages.docker_messages['Step_1'], parse_mode="Markdown")
    await callback.message.answer(".", reply_markup=bot_keyboard.get_docker_installation_kb())
    await callback.answer()


@router.callback_query(text="docker_2")
async def docker_step_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_messages.docker_messages['Step_2'], parse_mode="Markdown")
    await callback.message.answer(".", reply_markup=bot_keyboard.get_docker_installation_kb())
    await callback.answer()


@router.callback_query(text="docker_3")
async def docker_step_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_messages.docker_messages['Step_3_0'], parse_mode="Markdown")
    await callback.message.answer(bot_messages.docker_messages['Step_3_1'], parse_mode="Markdown")
    await callback.message.answer(".", reply_markup=bot_keyboard.get_docker_installation_kb())
    await callback.answer()


@router.callback_query(text="docker_4")
async def docker_step_4(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_messages.docker_messages['Step_4'], parse_mode="Markdown")
    await callback.message.answer(".", reply_markup=bot_keyboard.get_docker_installation_kb())
    await callback.answer()


@router.callback_query(text="docker_logs")
async def docker_logs(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_messages.docker_messages['logs'], parse_mode="Markdown")
    await callback.message.answer("Logs examples", reply_markup=bot_keyboard.get_docker_logs_kb())
    await state.update_data(menu='logs_example')
    await callback.answer()


@router.callback_query(text="docker_nodes_logs")
async def docker_node_logs(callback: types.CallbackQuery, state: FSMContext):
    node_img = FSInputFile('media/node_ex.png')
    await SendPhoto(chat_id=callback.message.chat.id, photo=node_img)
    await callback.answer()


@router.callback_query(text="docker_farmer_logs")
async def docker_farmer_logs(callback: types.CallbackQuery, state: FSMContext):
    farmer_img = FSInputFile('media/farmer_ex.png')
    await SendPhoto(chat_id=callback.message.chat.id, photo=farmer_img)
    await callback.answer()


@router.callback_query(text="docker_update")
async def docker_update(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_messages.docker_messages['Docker_update'], parse_mode="Markdown")
    await callback.answer()
