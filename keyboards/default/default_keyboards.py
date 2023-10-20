from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


free_check = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Get Free Check To My Account")
        ]
    ], resize_keyboard=True
)

send_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Send Phone Number", request_contact=True)
        ]
    ],resize_keyboard=True
)

my_scores = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐ My Scores")
        ]
    ], resize_keyboard=True
)

