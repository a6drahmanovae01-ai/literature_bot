import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN
import json
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Загрузка данных ---
with open("literature_quiz.json", "r", encoding="utf-8") as f:
    quiz_data = json.load(f)

with open("olympiad_questions.json", "r", encoding="utf-8") as f:
    olympiad_data = json.load(f)


@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "👋 Привет! Я бот для викторин, тестов и олимпиадных задач по литературе.\n\n"
        "📌 Доступные команды:\n"
        "/quiz – Викторина\n"
        "/test – Тест\n"
        "/olympiad – Олимпиадные задания\n"
        "/help – Помощь"
    )
    await message.answer(text)


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Я помогу тебе подготовиться к литературе 📚.\nИспользуй команды: /quiz /test /olympiad")


@dp.message(Command("quiz"))
async def quiz_command(message: types.Message):
    q = random.choice(quiz_data)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=a)] for a in q["options"]],
        resize_keyboard=True
    )
    await message.answer(q["question"], reply_markup=keyboard)


@dp.message(Command("test"))
async def test_command(message: types.Message):
    await message.answer("📖 Тесты пока в разработке, скоро будут добавлены!")


@dp.message(Command("olympiad"))
async def olympiad_command(message: types.Message):
    q = random.choice(olympiad_data)
    await message.answer(f"🏆 Олимпиадное задание:\n\n{q}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
