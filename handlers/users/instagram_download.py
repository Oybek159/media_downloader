from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from utils.instagram_service import downloader
from keyboards.inline_keyboards import get_music

router = Router()

data = ()

@router.message(F.text.startswith(("https://www.instagram.com/", "https://instagram.com")))
async def insta_downloader(msg: Message):
    await msg.answer("⌛️")
    global data
    data = downloader(link=msg.text)
    # await msg.answer(str(data))
    
    for type in data:
        if type == "error":
            await msg.answer("Invalid link")
        if type[0]["type"] == "image":
            await msg.answer_photo(photo=type[0]["media"])
        elif type[0]["type"] == "video":
            await msg.answer_video(video=type[0]["media"], reply_markup=get_music())

    
    
    # print(data)

@router.callback_query(F.data=="music")
async def get_video_func(call: CallbackQuery):
    for type in data:
        if type[0]["type"] == "audio":
            await call.message.answer_audio(audio=type[0]["audio"])
        else:
            await call.message.answer("Music not found")
