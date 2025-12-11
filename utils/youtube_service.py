import json
import os

import yt_dlp
from dotenv import load_dotenv

load_dotenv()

# def extract_video_id(url):
#     """
#     YouTube URL-laridan video ID ajratib beruvchi funksiya.
#     """
#     patterns = [
#         r"v=([a-zA-Z0-9_-]+)",  # Oddiy video
#         r"shorts/([a-zA-Z0-9_-]+)",  # YouTube Shorts
#         r"embed/([a-zA-Z0-9_-]+)",  # Embed video
#         r"youtu\.be/([a-zA-Z0-9_-]+)",  # Youtu.be short link
#         r"live/([a-zA-Z0-9_-]+)"  # YouTube Live Stream
#     ]
#
#     for pattern in patterns:
#         match = re.search(pattern, url)
#         if match:
#             return match.group(1)
#
#     return None
#
# def downloader(link):
#     url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
#     youtube_api = os.getenv("YOUTUBE_API")
#
#     querystring = {"videoId": extract_video_id(url=link)}
#     headers = {
#         "x-rapidapi-key": youtube_api,
#         "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
#     }
#
#     response = requests.get(url, headers=headers, params=querystring)
#
#     result = response.json()
#
#     result1 = result["videos"]["items"][0]["url"]
#     return result1
    

# print(downloader("https://www.youtube.com/live/NwXX9kkEMi4?si=3_AySpKZYLcRSYVA"))

def downloader(user_dict: dict, output_path="media/yt_videos"):
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    for user_id, video_url in user_dict.items():
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            "outtmpl": f"{output_path}/{user_id}_video.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            ydl.download([video_url])

            # ℹ️ ydl.sanitize_info makes the info json-serializable
            print(json.dumps(ydl.sanitize_info(info)))




