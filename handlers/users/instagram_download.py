from aiogram import Router, F
from aiogram.types import Message
from utils.instagram_service import downloader

router = Router()

@router.message(F.text.startswith(("https://www.instagram.com/", "https://instagram.com")))
async def insta_downloader(msg: Message):
    await msg.answer("⌛️")
    data = downloader(link=msg.text)
    
    for type in data:
        if type == "error":
            await msg.answer("Invalid link")
        if type["type"] == "image":
            await msg.answer_photo(photo=type["media"])
        elif type["type"] == "video":
            await msg.answer_video(video=type["media"])
    print(data)