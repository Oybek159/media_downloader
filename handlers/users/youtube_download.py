from aiogram import Router, F
from aiogram.types import Message
from utils.youtube_service import extract_video_id, downloader

router = Router()

@router.message(F.text.startswith("https://you"))
async def youtube_download(msg: Message):
    video_url = msg.text
    await msg.answer("⌛️")

    download_link = downloader(video_url)
    if download_link:
        await msg.answer_video(video=download_link)
    else:
        await msg.answer("Invalid link")
