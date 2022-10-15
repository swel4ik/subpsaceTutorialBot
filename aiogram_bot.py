import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5384669677:AAHepwAcMJWbcoesDOtC3jiqzty3ztsbGR8")
# Диспетчер
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text='📡Set up your nodes📡')],
        [types.KeyboardButton(text='🛠Machine requirements🛠')],
        [types.KeyboardButton(text='❓FAQ❓')]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Choose"
    )
    await message.answer("What you are interested in?", reply_markup=keyboard)


@dp.message_handler(Text(contains='📡Set up your nodes📡'))
async def with_puree(message: types.Message):
    await message.reply("Got it", reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text='Docker 🐳')],
        [types.KeyboardButton(text='Linux CLI 🖥')],
        [types.KeyboardButton(text='Windows 💾')]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Choose installation type"
    )
    await message.answer("Choose installation type", reply_markup=keyboard)


@dp.message_handler(Text(contains='Docker 🐳'))
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Step 0: Requirements | Wallet')],
        [types.KeyboardButton(text='Step 1: Installing necessary server tools')],
        [types.KeyboardButton(text='Step 2: Check | Open necessary TCP ports')],
        [types.KeyboardButton(text='Step 3: Configure your config')],
        [types.KeyboardButton(text='Step 4: Set up and run your nodes')],
        [types.KeyboardButton(text='Check logs')]
    ]
    keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder="Choose installation step"
        )
    await message.answer("Choose installation step", reply_markup=keyboard)


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