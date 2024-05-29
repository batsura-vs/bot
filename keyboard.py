from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from user_states import UserStates


def get_keyboard(state):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=name) for name in buttons]
            for buttons in state
        ],
        resize_keyboard=True
    )


keyboard = {
    UserStates.BASE: get_keyboard([["Мои пари"], ["Создать пари"]]),
}
