import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from messages import BotMessages
from keyboards import BotKeyboards

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5384669677:AAHepwAcMJWbcoesDOtC3jiqzty3ztsbGR8")
# Диспетчер
dp = Dispatcher(bot=bot)
bot_messages = BotMessages()
bot_keyboard = BotKeyboards()


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=bot_keyboard.start_kb,
        resize_keyboard=True,
        input_field_placeholder="Choose"
    )
    await message.answer("What you are interested in?", reply_markup=keyboard)


@dp.message_handler(Text(contains='📡Set up your nodes📡'))
async def with_puree(message: types.Message):
    await message.reply("Got it", reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=bot_keyboard.installation_type_kb,
        resize_keyboard=True,
        input_field_placeholder="Choose installation type"
    )
    await message.answer("Choose installation type", reply_markup=keyboard)


@dp.message_handler(Text(contains='Docker 🐳'))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
            keyboard=bot_keyboard.docker_steps_kb,
            resize_keyboard=True,
            input_field_placeholder="Choose installation step"
        )
    await message.answer("Choose installation step", reply_markup=keyboard)


@dp.message_handler(Text(contains='Step 0: Requirements | Wallet'))
async def with_puree(message: types.Message):

    wallet_img = open('media/wallet_ex.png', 'rb')
    await message.answer(bot_messages.docker_messages['Step_0_0'], parse_mode="Markdown")
    await message.answer(bot_messages.docker_messages['Step_0_1'], parse_mode="Markdown")
    await bot.send_photo(message.chat.id, wallet_img)


@dp.message_handler(Text(contains='Step 1: Installing necessary server tools'))
async def with_puree(message: types.Message):
    await message.answer(bot_messages.docker_messages['Step_1'], parse_mode="Markdown")


@dp.message_handler(Text(contains='Step 2: Check | Open necessary TCP ports'))
async def with_puree(message: types.Message):
    await message.answer(bot_messages.docker_messages['Step_2'], parse_mode="Markdown")


@dp.message_handler(Text(contains='Step 3: Configure your nodes'))
async def with_puree(message: types.Message):
    await message.answer(bot_messages.docker_messages['Step_3_0'], parse_mode="Markdown")
    await message.answer(bot_messages.docker_messages['Step_3_1'], parse_mode="Markdown")
    release_img = open('media/release_ex.png', 'rb')
    await bot.send_photo(message.chat.id, release_img)


@dp.message_handler(Text(contains='Step 4: Set up and run your nodes'))
async def with_puree(message: types.Message):
    await message.answer(bot_messages.docker_messages['Step_4'], parse_mode="Markdown")


@dp.message_handler(Text(contains='Check logs'))
async def with_puree(message: types.Message):
    await message.answer(bot_messages.docker_messages['logs'], parse_mode="Markdown")

    kb = [
        [types.KeyboardButton(text='Example of node successfully logs 📡')],
        [types.KeyboardButton(text='Example of farmer successfully logs 👨‍🌾')]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Logs examples", reply_markup=keyboard)


@dp.message_handler(Text(contains='Example of node successfully logs 📡'))
async def with_puree(message: types.Message):
    node_img = open('media/node_ex.png', 'rb')
    await bot.send_photo(message.chat.id, node_img)


@dp.message_handler(Text(contains='Example of farmer successfully logs 👨‍🌾'))
async def with_puree(message: types.Message):
    farmer_img = open('media/farmer_ex.png', 'rb')
    await bot.send_photo(message.chat.id, farmer_img)


@dp.message_handler(Text(contains='🛠Machine requirements🛠'))
async def with_puree(message: types.Message):
    bot_mes = "CPU: 2 Core+\nRAM: 4GB+(Rec. 8GB)\nStorage: 150 GB"
    await message.reply(bot_mes)




@dp.message_handler()
async def echo_message(msg: types.Message):
    text = "Write /start for bot activation"
    await bot.send_message(msg.from_user.id, text)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())