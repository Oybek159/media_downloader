# import requests
# from aiogram import Router, F
# from aiogram.types import CallbackQuery, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
# from shazamio import Shazam
# from yt_dlp import YoutubeDL
#
# from handlers.users.instagram_download import user_instagram_data, instagram_link
#
# shazam = Shazam()
# router = Router()
#
# user_tracks = {}
#
# @router.callback_query(F.data=="music")
# async def get_video_func(call: CallbackQuery):
#     print(user_instagram_data)
#     user_id = call.from_user.id
#     video_url = user_instagram_data[user_id]
#     response = requests.get(video_url)
#     print(response)
#
#     with open(f"{user_id}_video.mp4", "wb") as f:
#         f.write(response.content)
#
#     result = await shazam.recognize(f"{user_id}_video.mp4")
#     if result and "track" in result:
#         track = result["track"]
#         track_id = track["key"]
#         related = await shazam.related_tracks(track_id=track_id, limit=10, offset=2)
#         print(related)
#
#         user_tracks[user_id] = related["tracks"]
#
#         message_text = "🎵 **Similar Tracks:**\n\n"
#         buttons = []
#
#         for count, track in enumerate(related["tracks"], start=1):
#             artist = track["subtitle"]
#             title = track["title"]
#             message_text += f"{count}. {artist} - {title}\n"
#
#             buttons.append(
#                 InlineKeyboardButton(text=f"{count}",
#                                      callback_data=f"download_{count-1}")
#             )
#         keyboard = InlineKeyboardMarkup(inline_keyboard=[
#            buttons[:5],
#             buttons[5:]
#         ])
#         await call.message.answer(text=message_text, parse_mode="Markdown", reply_markup=keyboard)
#
#
# @router.callback_query(F.data.startswith("download_"))
# async def send_music(call: CallbackQuery):
#     user_id = call.from_user.id
#     track_index = int(call.data.split("_")[1])
#
#     track = user_tracks[user_id][track_index]
#     artist = track["subtitle"]
#     title = track["title"]
#
#     search_query = f"{title} {artist} audio"
#
#     ydl_opts = {
#         "format": "bestaudio/best",
#         "postprocessors": [{
#             "key": "FFmpegExtractAudio",
#             "preferredcodec": "mp3",
#             "preferredquality": "192"
#         }],
#         "outtmpl": f"{user_id}_audio.%(ext)s",
#     }
#
#     with YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(f"ytsearch:{search_query}", download=True)
#
#     audio = FSInputFile(f"{user_id}_audio.mp3")
#     await call.message.answer_audio(audio=audio, title=title, performer=artist)
#
#
#     # print(result["track"]["hub"]["actions"][1]["uri"])
#
#
#
#
