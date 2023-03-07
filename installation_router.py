from aiogram import Router
from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext
from messages import BotMessages
from keyboards import BotKeyboards
from utils import BotStates

bot_messages = BotMessages()
bot_keyboard = BotKeyboards()
router = Router()


@router.callback_query(text='docker_install')
async def docker_installation(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Choose installation step", reply_markup=bot_keyboard.get_docker_installation_kb())
    await state.set_state(BotStates.choosing_docker_steps)
    await state.update_data(menu='installation_step')
    await callback.answer()


@router.callback_query(text='subspace_cli')
async def docker_installation(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Choose installation step", reply_markup=bot_keyboard.get_docker_installation_kb())
    await state.set_state(BotStates.choosing_subspace_cli_steps)
    await state.update_data(menu='installation_step_subspace')
    await callback.answer()
