import asyncio
import random
import json
from datetime import datetime

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

HER_ID = 2007593176
MY_ID = 1395307876

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
    "ялюблютебятаксильнотыпростонеможешьпредставитьадумаюотебекаждуюсекунду",
    "самой красивой и шикарной девушке хочу сказать я очень сильно её ценю и обожаю, как мне с ней повезло и как же она красива и прекрасна… 143",
    "я не могу поверить что ты реальная, неужели такая идеальная девушка как ты действительно существует… я никогда не видел таких красивых девочек… не я серьезно… 143…",
    "Я ТЕБЯ ПРОСТО ОБОЖАЮ МОЯ ХОРОШЕНЬКАЯ!!! Я ОЧЕНЬ ХОЧУ ТЕБЯ ОБНИМАТЬ И ЦЕЛОВАТЬ!!! ОЧЕНЬ ТЕБЯ ЛЮБЛЮ!! 143!!",
    "ты у меня самая любименькая красивая и прекрасная!! я очень тебя люблю ариша!!!!! 143",
    "я не верю что ты можешь быть такой красивой(( может я просто сплю? ты безусловно заслужила эту красоту, но я не верю, что это просто возможно ваще… 143"
]

MONOLOG = "солнце мое я уже стал путаться я хоть когда-то вообще не думаю о тебе или как? я не знаю как описать эти чувства не то что текстом, я не уверен что я даже тактильно смогу показать то насколько тебя люблю. это что-то большее чем просто чувства. я не знаю просто что это… я с каждым днем только чаще думаю о том, какая ты хорошая и о том как я тебя люблю.. а особенно о том, какая ты красивая, у меня по ощущению одно полушарие полностью этими мыслями занято ахахаха. я просто не знаю даже как вообще описать какой я тебя вижу. просто, идеальной? все равно не полностью описано. ну типа, я восхищаюсь каждой частичкой твоей внешности: твоими красивыми глазами, ресницами, твоими шелковыми волосами, красивыми губами, носику, но главное конечно, что из этого получается просто до безумия красивое и милое лицо. я готов смотреть на тебя вечность, правда. у тебя самая милая улыбка. прям ну очень. а если ты и не улыбаешься, то ты по прежнему остаешься самой красивой на свете. но лучше конечно, чтобы ты улыбалась. если ты счастлива, то и я счастлив. ты лучшее что со мной случалось, сколько бы я раз об этом не говорил. моя любовь к тебе просто бесконечна. я очень тебя люблю, моя хорошая. обожаю всем сердцем. еще раз, ты самая красивая, милая, добрая, смешная, и всеми хорошими качествами которые я только могу перечислить, ты обладаешь на максимум. люблю тебя безумно, даже если ты и не забывала это, все равно напомню. ты у меня самая любименькая. от серёжки. 143"

# -------------------- DATA --------------------

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {
            str(MY_ID): {"enabled": False, "waiting_send": False},
            str(HER_ID): {"enabled": False, "waiting_send": False}
        }

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

def ensure_user(user_id):
    if str(user_id) not in data:
        data[str(user_id)] = {"enabled": False, "waiting_send": False}
        save_data()

# -------------------- ACCESS --------------------

def is_allowed(user_id):
    return user_id in [HER_ID, MY_ID]

def other_user(user_id):
    return HER_ID if user_id == MY_ID else MY_ID

# -------------------- KEYBOARDS --------------------

def reply_keyboard(user_id):
    ensure_user(user_id)

    enabled = data[str(user_id)]["enabled"]
    waiting = data[str(user_id)]["waiting_send"]

    reminder_text = "выключить напоминания" if enabled else "включить напоминания"

    keyboard = [
        [KeyboardButton(text="обнять"), KeyboardButton(text="поцеловать")],
        [KeyboardButton(text=reminder_text)]
    ]

    if user_id == MY_ID:
        if waiting:
            keyboard.append([KeyboardButton(text="отмена")])
        else:
            keyboard.append([KeyboardButton(text="сообщение")])

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def inline_keyboard(user_id):
    enabled = data[str(user_id)]["enabled"]
    if enabled:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="выключить напоминания", callback_data="stop")]]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="включить напоминания", callback_data="enable")]]
        )

# -------------------- START --------------------

@dp.message(Command("start"))
async def start(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    ensure_user(message.from_user.id)

    await message.answer(
        "ну шо ты косолапая",
        reply_markup=reply_keyboard(message.from_user.id)
    )

    await message.answer(
        " ",
        reply_markup=inline_keyboard(message.from_user.id)
    )

# -------------------- ENABLE/DISABLE --------------------

@dp.callback_query(F.data == "enable")
async def enable(callback: types.CallbackQuery):
    if not is_allowed(callback.from_user.id):
        return

    user_id = callback.from_user.id
    ensure_user(user_id)

    data[str(user_id)]["enabled"] = True
    save_data()

    await callback.message.answer(
        "уряяя!! 143143143!!!! теперь ты точно никогда не забудешь о том как я тебя люблю!",
        reply_markup=reply_keyboard(user_id)
    )

    await callback.message.answer(
        " ",
        reply_markup=inline_keyboard(user_id)
    )

    await callback.answer()

@dp.callback_query(F.data == "stop")
async def stop(callback: types.CallbackQuery):
    if not is_allowed(callback.from_user.id):
        return

    user_id = callback.from_user.id
    ensure_user(user_id)

    data[str(user_id)]["enabled"] = False
    save_data()

    await callback.message.answer(
        "ну блин, я понимаю что ты это и так знаешь, но всё же..( ну лан, надеюсь тебе понравилось!",
        reply_markup=reply_keyboard(user_id)
    )

    await callback.message.answer(
        " ",
        reply_markup=inline_keyboard(user_id)
    )

    await callback.answer()

@dp.message(F.text == "включить напоминания")
async def enable_text(message: types.Message):
    await enable(types.CallbackQuery(
        id="text",
        from_user=message.from_user,
        chat_instance="",
        message=message,
        data="enable"
    ))

@dp.message(F.text == "выключить напоминания")
async def disable_text(message: types.Message):
    await stop(types.CallbackQuery(
        id="text",
        from_user=message.from_user,
        chat_instance="",
        message=message,
        data="stop"
    ))

# -------------------- SEND MODE --------------------

@dp.message(Command("send"))
@dp.message(F.text == "сообщение")
async def enter_send(message: types.Message):
    if message.from_user.id != MY_ID:
        return

    data[str(MY_ID)]["waiting_send"] = True
    save_data()

    await message.answer(
        "напиши чонить",
        reply_markup=reply_keyboard(MY_ID)
    )

@dp.message(F.text == "отмена")
@dp.message(Command("cancel"))
async def cancel_send(message: types.Message):
    if message.from_user.id != MY_ID:
        return

    data[str(MY_ID)]["waiting_send"] = False
    save_data()

    await message.answer(
        "откат",
        reply_markup=reply_keyboard(MY_ID)
    )

# -------------------- HUG / KISS --------------------

@dp.message(Command("hug"))
@dp.message(F.text == "обнять")
async def hug(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    if data[str(message.from_user.id)]["waiting_send"]:
        return

    await message.answer("обнимашки переданы!!")
    await bot.send_message(other_user(message.from_user.id), "тебя обняли!!")

@dp.message(Command("kiss"))
@dp.message(F.text == "поцеловать")
async def kiss(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    if data[str(message.from_user.id)]["waiting_send"]:
        return

    await message.answer("поцелуй передан!")
    await bot.send_message(other_user(message.from_user.id), "тебя поцеловали!")

# -------------------- TEXT HANDLER --------------------

@dp.message(F.text)
async def text_handler(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    user_id = message.from_user.id
    ensure_user(user_id)

    # если режим send
    if user_id == MY_ID and data[str(MY_ID)]["waiting_send"]:
        await bot.send_message(HER_ID, message.text)
        data[str(MY_ID)]["waiting_send"] = False
        save_data()
        await message.answer("отправил", reply_markup=reply_keyboard(MY_ID))
        return

    text = message.text

    if text == "143":
        await message.answer("1432")

    elif text == "я тебя люблю":
        await message.answer("я тебя тоже")

    elif text == "я люблю тебя":
        await message.answer("и я тебя")

    elif text in ["я люблю сережу", "я люблю серёжу"]:
        await message.answer("а я люблю аришу")

# -------------------- SCHEDULER --------------------

last_sent = {}

async def reminder_loop():
    await asyncio.sleep(5)

    while True:
        now = datetime.now(OMSK_TZ)
        key = f"{now.hour}:{now.minute}"

        for user_id in [MY_ID, HER_ID]:
            ensure_user(user_id)

            if not data[str(user_id)]["enabled"]:
                continue

            if last_sent.get((user_id, key)):
                continue

            # 6:24 и 1:43
            if (now.hour == 6 and now.minute == 24) or (now.hour == 1 and now.minute == 43):
                await bot.send_message(user_id, random.choice(MESSAGES))
                last_sent[(user_id, key)] = True

            # 14:43 — 10%
            if now.hour == 14 and now.minute == 43:
                if random.random() <= 0.10:
                    await bot.send_message(user_id, "💋")
                last_sent[(user_id, key)] = True

            # Нечётные часы — 1%
            if now.minute == 43 and now.hour % 2 == 1:
                if random.random() <= 0.01:
                    await bot.send_message(user_id, MONOLOG)
                last_sent[(user_id, key)] = True

        await asyncio.sleep(20)

# -------------------- RUN --------------------

async def main():
    asyncio.create_task(reminder_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
