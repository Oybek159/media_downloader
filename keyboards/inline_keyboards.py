from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_music():
    btn1 = InlineKeyboardButton(text="Get Music", callback_data="music")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [btn1]
        ]
    )
    return ikm