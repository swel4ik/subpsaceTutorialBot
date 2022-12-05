from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import StatesGroup, State
from aiogram.utils.helper import Helper, HelperMode, ListItem


class BotStates(StatesGroup):
    main_menu = State()
    choosing_installation_type = State()
    choosing_docker_steps = State()
    user_problem = State()
    req_info = State()


class BotStatesCustom:
    def __init__(self):
        self.active_state = None

