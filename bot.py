import asyncio
import random
import json
from datetime import datetime, timedelta

import pytz
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

TOKEN = "8279523638:AAFQoHMem4XCW2eq3fdcC0nmMbHysJsrED4"

HER_ID = 2007593176   # ВСТАВЬ ЕЁ ID
MY_ID = 1395307876    # ВСТАВЬ СВОЙ ID

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
    "ялюблютебятаксильнотыпростонеможешьпредставитьадумаюотебекаждуюсекунду"
]

MONOLOG = """«солнце мое я уже стал путаться я хоть когда-то вообще не думаю о тебе или как? я не знаю как описать эти чувства не то что текстом, я не уверен что я даже тактильно смогу показать то насколько тебя люблю. это что-то большее чем просто чувства. я не знаю просто что это… я с каждым днем только чаще думаю о том, какая ты хорошая и о том как я тебя люблю.. а особенно о том, какая ты красивая, у меня по ощущению одно полушарие полностью этими мыслями занято ахахаха. я просто не знаю даже как вообще описать какой я тебя вижу. просто, идеальной? все равно не полностью описано. ну типа, я восхищаюсь каждой частичкой твоей внешности: твоими красивыми глазами, ресницами, твоими шелковыми волосами, красивыми губами, носику, но главное конечно, что из этого получается просто до безумия красивое и милое лицо. я готов смотреть на тебя вечность, правда. у тебя самая милая улыбка. прям ну очень. а если ты и не улыбаешься, то ты по прежнему остаешься самой красивой на свете. но лучше конечно, чтобы ты улыбалась. если ты счастлива, то и я счастлив. ты лучшее что со мной случалось, сколько бы я раз об этом не говорил. моя любовь к тебе просто бесконечна. я очень тебя люблю, моя хорошая. обожаю всем сердцем. еще раз, ты самая красивая, милая, добрая, смешная, и всеми хорошими качествами которые я только могу перечислить, ты обладаешь на максимум. люблю тебя безумно, даже если ты и не забывала это, все равно напомню. ты у меня самая любименькая. от серёжки. 143»"""  # вставь свой полный текст

# ---------- Работа с файлом ----------

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"chat_id": None, "reminders_enabled": False}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# ---------- Проверка доступа ----------

def is_allowed(user_id):
    return user_id in [HER_ID, MY_ID]

def other_user(user_id):
    return HER_ID if user_id == MY_ID else MY_ID

# ---------- Клавиатура ----------

def reply_keyboard():
    reminder_text = "выключить напоминания" if data["reminders_enabled"] else "включить напоминания"
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="обнять"), KeyboardButton(text="поцеловать")],
            [KeyboardButton(text=reminder_text)]
        ],
        resize_keyboard=True
    )

def inline_keyboard():
    if data["reminders_enabled"]:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="выключить напоминания", callback_data="stop")]]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="включить напоминания", callback_data="enable")]]
        )

# ---------- /start ----------

@dp.message(Command("start"))
async def start(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    data["chat_id"] = message.chat.id
    save_data(data)
    await message.answer("ну шо ты косолапая", reply_markup=reply_keyboard())
    await message.answer(" ", reply_markup=inline_keyboard())

# ---------- Inline ----------

@dp.callback_query(F.data == "enable")
async def enable(callback: types.CallbackQuery):
    if not is_allowed(callback.from_user.id):
        return
    data["reminders_enabled"] = True
    save_data(data)
    await callback.message.answer(
        "уряяя!! 143143143!!!! теперь ты точно никогда не забудешь о том как я тебя люблю!",
        reply_markup=reply_keyboard()
    )
    await callback.answer()

@dp.callback_query(F.data == "stop")
async def stop(callback: types.CallbackQuery):
    if not is_allowed(callback.from_user.id):
        return
    data["reminders_enabled"] = False
    save_data(data)
    await callback.message.answer("ну блин, я понимаю что ты это и так знаешь, но всё же( ну лан, надеюсь тебе понравилось!")
    await callback.answer()

# ---------- Текстовые кнопки ----------

@dp.message(F.text == "включить напоминания")
async def enable_text(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    data["reminders_enabled"] = True
    save_data(data)
    await message.answer(
        "уряяя!! 143143143!!!! теперь ты точно никогда не забудешь о том как я тебя люблю!",
        reply_markup=reply_keyboard()
    )

@dp.message(F.text == "выключить напоминания")
async def disable_text(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    data["reminders_enabled"] = False
    save_data(data)
    await message.answer("ну блин, я понимаю что ты это и так знаешь, но всё же( ну лан, надеюсь тебе понравилось!")
    
# ---------- Hug / Kiss ----------

@dp.message(Command("hug"))
@dp.message(F.text == "обнять")
async def hug(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    await message.answer("обнимашки переданы!!")
    await bot.send_message(other_user(message.from_user.id), "тебя обняли!!")

@dp.message(Command("kiss"))
@dp.message(F.text == "поцеловать")
async def kiss(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    await message.answer("поцелуй передан!")
    await bot.send_message(other_user(message.from_user.id), "тебя поцеловали!")

# ---------- Строгие триггеры ----------

@dp.message(F.text)
async def strict_triggers(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    text = message.text

    if text == "143":
        await message.answer("1432")

    elif text == "я тебя люблю":
        await message.answer("я тебя тоже")

    elif text == "я люблю тебя":
        await message.answer("и я тебя")

    elif text == "я люблю сережу" or text == "я люблю серёжу":
        await message.answer("а я люблю аришу")

# ---------- Scheduler ----------

last_sent = None

async def reminder_loop():
    global last_sent
    await asyncio.sleep(5)

    while True:
        if not data["reminders_enabled"] or not data["chat_id"]:
            await asyncio.sleep(30)
            continue

        now = datetime.now(OMSK_TZ)
        key = f"{now.hour}:{now.minute}"

        # 6:24 и 1:43
        if now.minute in [24, 43] and key != last_sent:
            if (now.hour == 6 and now.minute == 24) or (now.hour == 1 and now.minute == 43):
                text = random.choice(MESSAGES)
                await bot.send_message(data["chat_id"], text)
                last_sent = key

        # 14:43 — 10%
        if now.hour == 14 and now.minute == 43 and key != last_sent:
            if random.random() <= 0.10:
                await bot.send_message(data["chat_id"], "💋")
            last_sent = key

        # Нечётные часы — 1%
        if now.minute == 43 and now.hour % 2 == 1 and key != last_sent:
            if random.random() <= 0.01:
                await bot.send_message(data["chat_id"], MONOLOG)
            last_sent = key

        await asyncio.sleep(20)

# ---------- /send для админа ----------

@dp.message(Command("send"))
async def send_to_her(message: types.Message):
    if message.from_user.id != MY_ID:
        return  # Только для твоего ID
    # Получаем текст после команды /send
    text = message.get_args()  # Возьмёт всё после "/send "
    if not text:
        await message.answer("ну ты текст то напиши")
        return
    await bot.send_message(HER_ID, text)
    await message.answer(f"отправил: {text}")

# ---------- Запуск ----------

async def main():
    asyncio.create_task(reminder_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
