import asyncio
import random
import json
from datetime import datetime, timedelta

import pytz
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8279523638:AAFQoHMem4XCW2eq3fdcC0nmMbHysJsrED4"  # токен от @BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher()

DATA_FILE = "data.json"
OMSK_TZ = pytz.timezone("Asia/Omsk")

MESSAGES = [
    "я тебя очень люблю ты помнишь да? 143",
    "я люблю тебя больше всех на свете аришк!! 143",
    "ты самая лучшая на свете девочка я очень люблю тебя!! 143",
    "если можно это сообщение как-то передать этой богине, то передайте ей пожалуйста что я её очень люблю. 143",
    "самой красивой и милой девочке: я люблю тебя!! (от серёжи) 143",
    "у меня просто эйфория от твоей красоты у тебя такая милая улыбка я тебя очен лублу. 143",
    "143243447155356",
    "ну уж очень я люблю эту косолапую емае чеж делать то.. 143",
    "ты у меня самая любимая на свете!! 143",
    "заявляю со стопроцентной уверенностью: серёжа сейчас думает о том какая ты красивая. 143",
    "у тебя самая прекрасная улыбка которую я видел, ты мне заменяешь солнце. 143",
    "я никогда не был так счастлив просто от наличия человека в моей жизни.. я очень тебя люблю! 143",
    "прямо сейчас я думаю о тебе. я очень люблю тебя ариш. 143",
    "я не знаю как я раньше жил без тебя моя хорошая.. 143",
    "143143143143143143143143143143143143143143",
    "самой косолапенькой из всех косолапых передаю свою бесконечную любовь!! 143",
    "я тебя безумно люблю. это навсегда, я уверен!! 143",
    "светись также ярко как и сейчас, моя любимая. 143",
    "самой любименькой на свете аришке хочу сказать что я её очень сильно люблю и обожаю!!! 143",
    "ялюблютебятаксильнотыпростонеможешьпредставитьядумаюотебекаждуюсекунду"
    # добавь свои 20 сообщений
]

# ---------- Работа с файлом ----------

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"chat_id": None, "reminders_enabled": False}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# ---------- Кнопки ----------

def start_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="включить напоминания", callback_data="enable"),
                InlineKeyboardButton(text="не включать напоминания", callback_data="disable")
            ]
        ]
    )
    return kb

def stop_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="выключить напоминания", callback_data="stop")
            ]
        ]
    )
    return kb

# ---------- /start ----------

@dp.message(Command("start"))
async def start(message: types.Message):
    data["chat_id"] = message.chat.id
    save_data(data)
    await message.answer("ну шо ты косолапая", reply_markup=start_keyboard())

# ---------- Кнопки ----------

@dp.callback_query(lambda c: c.data == "disable")
async def disable(callback: types.CallbackQuery):
    await callback.message.answer("ну блин, я понимаю что ты это и так знаешь, но всё же(")
    await callback.answer()

@dp.callback_query(lambda c: c.data == "enable")
async def enable(callback: types.CallbackQuery):
    data["reminders_enabled"] = True
    save_data(data)
    await callback.message.answer(
        "уряяя!! 143143143!!!! теперь ты точно никогда не забудешь о том как я тебя люблю!",
        reply_markup=stop_keyboard()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "stop")
async def stop(callback: types.CallbackQuery):
    data["reminders_enabled"] = False
    save_data(data)
    await callback.message.answer("ну, надеюсь, тебе понравилось")
    await callback.answer()

# ---------- 143 -> 1432 ----------

@dp.message()
async def handle_text(message: types.Message):
    if message.text.strip() == "143":
        await message.answer("1432")

# ---------- Фоновая задача ----------

async def reminder_loop():
    await asyncio.sleep(5)
    while True:
        if not data.get("reminders_enabled") or not data.get("chat_id"):
            await asyncio.sleep(60)
            continue

        now = datetime.now(OMSK_TZ)
        target_time = random.choice([
            now.replace(hour=6, minute=24, second=0, microsecond=0),
            now.replace(hour=1, minute=43, second=0, microsecond=0)
        ])
        if target_time <= now:
            target_time += timedelta(days=1)

        sleep_seconds = (target_time - now).total_seconds()
        await asyncio.sleep(sleep_seconds)

        if data.get("reminders_enabled"):
            text = random.choice(MESSAGES)
            await bot.send_message(data["chat_id"], text)

        await asyncio.sleep(60)

# ---------- Запуск ----------

async def main():
    asyncio.create_task(reminder_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

