from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from config import TOKEN
from keyboard import keyboard
from user_states import UserStates

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет! я умею следить за Пари", reply_markup=keyboard[UserStates.BASE])
    await state.set_state(UserStates.BASE)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
