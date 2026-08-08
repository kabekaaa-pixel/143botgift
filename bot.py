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

TOKEN = "8279523638:AAFvjbxoRvbsWo-HOJEOTj1Gn4q4eM_Ob9E"

HER_ID = 2007593176
MY_ID = 1395307876

bot = Bot(token=TOKEN)
dp = Dispatcher()

DATA_FILE = "data.json"
OMSK_TZ = pytz.timezone("Asia/Omsk")

MESSAGES = [
    "я безумно люблю тебя, аришечка! 143",
    "я очень тебя люблю моя хорошенькая!! обожаю проста!! 143",
    "ты самая чудесная девочка на свете, аришенька. самая замечательная. чудо просто. 143",
    "ты просто божественна. я восхищаюсь твоей красотой. я обожаю смотреть на тебя. и тебя обожаю, очень. люблю. 143",
    "самой миленькой девочке передайте пж: я тебя люблюююю!! очень сильно!! ты прекрасна!! 143",
    "я самый счастливый человек на свете. а знаешь почему? потому что у меня есть ты! только ты делаешь меня таким счастливым!! люблю!!! 143",
    "143243447155356",
    "эй. псс. касалапая. я тя люблю)) очен)) 143",
    "ты у меня самая любименькая девочка!! самая миленькая и красивая!! 143",
    "я кстати сейчас о тебе думаю)) понимаю, тупо это говорить, когда я все время о тебе думаю, но всё же. думаю о том что очень сильно люблю тебя, если точнее. воть. 143",
    "у тебя самая милая улыбка, которую я видел. я не могу не улыбаться, когда смотрю на тебя. ты прекрасна(( 143",
    "привет! хочу напомнить, что я рядом. и буду рядом всегда. и очень сильно люблю тебя. безумно. 143",
    "как обнял бы сейчас.. и вот не отпускал бы вообще. я тебя люблю, ариш. 143",
    "я люблю тебя!! ТЕБЯ люблю!! люблю! люблю люблю!!!! люблю люблю люблю!!! 143",
    "143143143143143143143143143143143143143143",
    "я люблю тебя в квадрате. люблю тебя в тысячной степени. бесконечно люблю тебя в бесконечной степени!! 143",
    "мы всегда будем вместе. просто хотел напомнить, мало ли забыла, ахахаха. люблю тебя, чудо мое. 143",
    "светись также ярко как и сейчас, моя любимая. 143",
    "ты самая чудесная, замечательная, прекрасная, красивая, милая, умная, веселая, добрая и комфортная девушка. за это всё я тебя и люблю. ну то есть, за любое твое качество. они все безупречны! 143",
    "ялюблютебятаксильнотыпростонеможешьпредставитьадумаюотебекаждуюсекунду",
    "ты просто безупречна... самая шикарная на свете девушка, и она досталась мне. ахуеть. я каждый день восхищаюсь тобой(( 143",
    "я влюблен в тебя, ариша. безумно влюблен. я обожаю все что с тобой связано. ты чудесна. люблю. очень люблю. 143",
    "я просто одержим тобой аришечка что ты со мной сделала ааааааа. 143",
    "до сих пор не могу поверить, что мне досталась такая любящая девочка. омагад просто. я обожаю тебя ваще. 143",
    "чудо мое, я люблю тебя. безумно сильно. ты лучшее что у меня есть, и будет. 143",
    "люблю люблю люблю люблю!!! люблю тебя люблю люблю тебяяя!!! люблю люблю люблюююю!! 143",
    "я верю что любовь существует если существуем мы!! я очень люблю тебя серек!!! 143",
    "любимая, привет. я рядом. всегда. помни. люблю тебя. 143"
]

MONOLOG = "солнце мое я уже стал путаться я хоть когда-то вообще не думаю о тебе или как? я не знаю как описать эти чувства не то что текстом, я не уверен что я даже тактильно смогу показать то насколько тебя люблю. это что-то большее чем просто чувства. я не знаю просто что это… я с каждым днем только чаще думаю о том, какая ты хорошая и о том как я тебя люблю.. а особенно о том, какая ты красивая, у меня по ощущению одно полушарие полностью этими мыслями занято ахахаха. я просто не знаю даже как вообще описать какой я тебя вижу. просто, идеальной? все равно не полностью описано. ну типа, я восхищаюсь каждой частичкой твоей внешности: твоими красивыми глазами, ресницами, твоими шелковыми волосами, красивыми губами, носику, но главное конечно, что из этого получается просто до безумия красивое и милое лицо. я готов смотреть на тебя вечность, правда. у тебя самая милая улыбка. прям ну очень. а если ты и не улыбаешься, то ты по прежнему остаешься самой красивой на свете. но лучше конечно, чтобы ты улыбалась. если ты счастлива, то и я счастлив. ты лучшее что со мной случалось, сколько бы я раз об этом не говорил. моя любовь к тебе просто бесконечна. я очень тебя люблю, моя хорошая. обожаю всем сердцем. еще раз, ты самая красивая, милая, добрая, смешная, и всеми хорошими качествами которые я только могу перечислить, ты обладаешь на максимум. люблю тебя безумно, даже если ты и не забывала это, все равно напомню. ты у меня самая любименькая. от серёжки. 143"

# -------------------- DATA --------------------

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    # гарантируем что пользователи есть
    for uid in [MY_ID, HER_ID]:
        uid = str(uid)
        if uid not in data:
            data[uid] = {
                "enabled": True,
                "waiting_send": False,
                "ever_used_reminder": True
            }

    return data
        
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()
save_data()

def ensure_user(user_id):
    if str(user_id) not in data:
        data[str(user_id)] = {
    "enabled": False,
    "waiting_send": False,
    "ever_used_reminder": False
}
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

    keyboard = [
        [KeyboardButton(text="обнять"), KeyboardButton(text="поцеловать")]
    ]

    # кнопку напоминаний показываем только если пользователь уже включал их
    if data[str(user_id)].get("ever_used_reminder", False):
        reminder_text = "выключить напоминания" if enabled else "включить напоминания"
        keyboard.append([KeyboardButton(text=reminder_text)])

    if user_id == MY_ID:
        if waiting:
            keyboard.append([KeyboardButton(text="отмена")])
        else:
            keyboard.append([KeyboardButton(text="сообщение")])

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# -------------------- START --------------------

@dp.message(Command("start"))
async def start(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    ensure_user(message.from_user.id)

    await message.answer(
        "ну шо ты косолапая",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="включить напоминания", callback_data="enable_first")]
            ]
        )
    )

    await message.answer(
        " ",
        reply_markup=reply_keyboard(message.from_user.id)
    )

# -------------------- ENABLE/DISABLE --------------------

@dp.callback_query(F.data == "enable_first")
async def enable_first(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    ensure_user(user_id)

    data[str(user_id)]["enabled"] = True
    data[str(user_id)]["ever_used_reminder"] = True
    save_data()

    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(
        "уряяя!! 143143143!!!! теперь ты точно никогда не забудешь о том как я тебя люблю!",
        reply_markup=reply_keyboard(user_id)
    )

    await callback.answer()

@dp.message(F.text == "включить напоминания")
async def enable_text(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    data[str(user_id)]["enabled"] = True
    data[str(user_id)]["ever_used_reminder"] = True
    save_data()

    await message.answer(
        "уряяя!! 143143143!!!! теперь ты точно никогда не забудешь о том как я тебя люблю!",
        reply_markup=reply_keyboard(user_id)
    )

@dp.message(F.text == "выключить напоминания")
async def disable_text(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    data[str(user_id)]["enabled"] = False
    save_data()

    await message.answer(
        "ну блин, я понимаю что ты это и так знаешь, но всё же..( ну лан, надеюсь тебе понравилось!",
        reply_markup=reply_keyboard(user_id)
    )
    
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
daily_choice = {}

async def reminder_loop():
    await asyncio.sleep(5)

    while True:
        now = datetime.now(OMSK_TZ)
        key = f"{now.date()}-{now.hour}:{now.minute}"

        for user_id in [MY_ID, HER_ID]:
            ensure_user(user_id)

            today = str(now.date())

            # если сегодня ещё не выбирали время — выбираем
            if daily_choice.get(user_id) != today:
                daily_choice[user_id] = today

                if random.random() < 0.5:
                    daily_choice[(user_id, "time")] = (1, 43)
                else:
                    daily_choice[(user_id, "time")] = (6, 24)

            if not data[str(user_id)]["enabled"]:
                continue

            if last_sent.get((user_id, key)):
                continue

            # --- выбранное время (1:43 ИЛИ 6:24) ---
            chosen_hour, chosen_minute = daily_choice.get(
                (user_id, "time"), (1, 43)
            )

            if now.hour == chosen_hour and now.minute == chosen_minute:
                await bot.send_message(user_id, random.choice(MESSAGES))
                last_sent[(user_id, key)] = True

            # --- 14:43 — 10% ---
            if now.hour == 14 and now.minute == 43:
                if random.random() <= 0.10:
                    await bot.send_message(user_id, "💋")
                last_sent[(user_id, key)] = True

            # --- Нечётные часы — 1% ---
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
