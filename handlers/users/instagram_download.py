from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from utils.instagram_service import downloader
from keyboards.inline_keyboards import get_music

router = Router()

user_instagram_data = {}
instagram_link = {}

@router.message(F.text.startswith(("https://www.instagram.com/", "https://instagram.com")))
async def insta_downloader(msg: Message):
    await msg.answer("⌛️")
    data = downloader(link=msg.text)


    # print(data)
    # print("--------------------------------------")

    user_id = msg.from_user.id
    # instagram_link["link"] = msg.text

    
    for type in data:
        if type == "error":
            await msg.answer("Invalid link")
        if type[0]["type"] == "image":
            await msg.answer_photo(photo=type[0]["media"])
        elif type[0]["type"] == "video":
            await msg.answer_video(video=type[0]["media"], reply_markup=get_music())
            user_instagram_data[user_id] = type[0]["media"]

    # print(data)
    
    

    
    
    # print(data)


