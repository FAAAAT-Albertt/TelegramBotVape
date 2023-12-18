"""create state for feedback part"""
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

class Form(StatesGroup):
    """class states for feedback info"""
    user_question = State()
    user_id = State()
    admin_answer = State()
