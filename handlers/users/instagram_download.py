import os

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from utils.instagram_service import downloader
from keyboards.inline_keyboards import get_music

router = Router()

user_dict = {}

@router.message(F.text.startswith(("https://www.instagram.com/", "https://instagram.com")))
async def insta_downloader(msg: Message):
    await msg.answer("⌛️")
    user_id = msg.from_user.id
    video_url = msg.text
    user_dict[user_id] = video_url
    downloader(user_dict)

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    media_dir = os.path.join(base_dir, 'media')
    video_dir = os.path.join(media_dir, 'insta_videos')
    video_file = os.path.join(video_dir, f'{user_id}_video.mp4')

    video = FSInputFile(path=video_file)

    await msg.answer_video(video=video)




    



