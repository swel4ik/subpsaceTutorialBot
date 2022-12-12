from aiogram import types


class BotKeyboards:

    def __init__(self):
        """Constructor"""
        self.language_kb = []
        self.start_kb = [
            [types.InlineKeyboardButton(text='📡Set up your nodes📡')],
            [types.InlineKeyboardButton(text='🛠Machine requirements🛠')],
            [types.InlineKeyboardButton(text='❌Cancel❌')]
        ]

        self.installation_type_kb = [
            [types.KeyboardButton(text='Subspace CLI (Recommended) ✅')],
            [types.KeyboardButton(text='Docker 🐳')],
            [types.KeyboardButton(text='Substrate CLI 🖥')],
            [types.KeyboardButton(text='Windows 🏙 (coming soon)')],
            [types.KeyboardButton(text='Back ◀️')],
            [types.KeyboardButton(text='❌Cancel❌')]
        ]

        self.docker_steps_kb = [
            [types.KeyboardButton(text='Step 0: Requirements | Wallet')],
            [types.KeyboardButton(text='Step 1: Installing necessary server tools')],
            [types.KeyboardButton(text='Step 2: Check | Open necessary TCP ports')],
            [types.KeyboardButton(text='Step 3: Configure your nodes')],
            [types.KeyboardButton(text='Step 4: Set up and run your nodes')],
            [types.KeyboardButton(text='Logs example')],
            [types.KeyboardButton(text='Docker update')],
            [types.KeyboardButton(text='Back ◀️')],
            [types.KeyboardButton(text='❌Cancel❌')]

        ]

        self.docker_logs_kb = [
            [types.KeyboardButton(text='Example of node successfully logs 📡')],
            [types.KeyboardButton(text='Example of farmer successfully logs 👨‍🌾')],
            [types.KeyboardButton(text='Back ◀️')],
            [types.KeyboardButton(text='❌Cancel❌')]
        ]

    def get_main_kb(self):
        buttons = [
            [types.InlineKeyboardButton(text="📡Set up your nodes📡", callback_data="installation_type_menu")],
            [types.InlineKeyboardButton(text="🛠Machine requirements🛠", callback_data="req")],
            [types.InlineKeyboardButton(text="❌Cancel❌", callback_data="cancel")],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def get_installation_kb(self):
        buttons = [
            [types.InlineKeyboardButton(text="Subspace CLI (Recommended) ✅", callback_data="subspace_cli")],
            [types.InlineKeyboardButton(text="Docker 🐳", callback_data="docker_install")],
            [types.InlineKeyboardButton(text="Substrate CLI 🖥", callback_data="substrate_cli")],
            [types.InlineKeyboardButton(text="❌Cancel❌", callback_data="cancel")],
        ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def get_docker_installation_kb(self):
        buttons = [
            [types.InlineKeyboardButton(text="Step 0: Requirements | Wallet", callback_data="docker_0")],
            [types.InlineKeyboardButton(text="Step 1: Installing necessary server tools", callback_data="docker_1")],
            [types.InlineKeyboardButton(text="Step 2: Check | Open necessary TCP ports", callback_data="docker_2")],
            [types.InlineKeyboardButton(text="Step 3: Configure your nodes", callback_data="docker_3")],
            [types.InlineKeyboardButton(text="Step 4: Set up and run your nodes", callback_data="docker_4")],
            [types.InlineKeyboardButton(text="Logs example", callback_data="docker_logs")],
            [types.InlineKeyboardButton(text="Docker update", callback_data="docker_update")],
            [types.InlineKeyboardButton(text="❌Cancel❌", callback_data="cancel")],
        ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard =buttons)
        return keyboard

    def get_docker_logs_kb(self):
        buttons = [
            [types.InlineKeyboardButton(text="Example of node successfully logs 📡", callback_data="docker_nodes_logs")],
            [types.InlineKeyboardButton(text="Example of farmer successfully logs 👨‍🌾", callback_data="docker_farmer_logs")],
            [types.InlineKeyboardButton(text="❌Cancel❌", callback_data="cancel")],
        ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard




