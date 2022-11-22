from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State
from aiogram.utils.helper import Helper, HelperMode, ListItem


class BotStates(StatesGroup):
    main_menu = State()
    choosing_installation_type = State()
    choosing_docker_steps = State()