from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove

API_TOKEN = ""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Keyboard removed.", reply_markup=ReplyKeyboardRemove())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
