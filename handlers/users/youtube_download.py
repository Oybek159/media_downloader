import os.path

from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from utils.youtube_service import downloader

router = Router()
user_dict = {}

@router.message(F.text.startswith("https://you"))
async def youtube_download(msg: Message):
    user_id = msg.from_user.id
    video_link = msg.text
    user_dict[user_id] = video_link
    downloader(user_dict)

    sticker_msg = await msg.answer("⌛️")

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    media_dir = os.path.join(base_dir, 'media')
    video_dir = os.path.join(media_dir, 'yt_videos')
    video_file = os.path.join(video_dir, f'{user_id}_video.mp4')

    video = FSInputFile(path=video_file)


    await msg.answer_video(video=video)
    # os.remove(path=video_file)
    await sticker_msg.delete()

