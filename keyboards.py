from aiogram import types


class BotKeyboards:

    def __init__(self):
        """Constructor"""

        self.start_kb = [
            [types.KeyboardButton(text='📡Set up your nodes📡')],
            [types.KeyboardButton(text='🛠Machine requirements🛠')],
            [types.KeyboardButton(text='❓FAQ❓')],
            [types.KeyboardButton(text='Cancel')]
        ]

        self.installation_type_kb = [
            [types.KeyboardButton(text='Docker 🐳')],
            [types.KeyboardButton(text='Linux CLI 🖥')],
            [types.KeyboardButton(text='Windows 🏙')],
            [types.KeyboardButton(text='Cancel')]
        ]

        self.docker_steps_kb = [
            [types.KeyboardButton(text='Step 0: Requirements | Wallet')],
            [types.KeyboardButton(text='Step 1: Installing necessary server tools')],
            [types.KeyboardButton(text='Step 2: Check | Open necessary TCP ports')],
            [types.KeyboardButton(text='Step 3: Configure your nodes')],
            [types.KeyboardButton(text='Step 4: Set up and run your nodes')],
            [types.KeyboardButton(text='Logs example')],
            [types.KeyboardButton(text='Docker update')],
            [types.KeyboardButton(text='Cancel')]

        ]

        self.docker_logs_kb = [
            [types.KeyboardButton(text='Example of node successfully logs 📡')],
            [types.KeyboardButton(text='Example of farmer successfully logs 👨‍🌾')]
        ]
