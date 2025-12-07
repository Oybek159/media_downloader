# import os
#
# import requests
# from dotenv import load_dotenv
#
# load_dotenv()
#
# instagram_api = os.getenv("INSTAGRAM_API")
# url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"
# querystring = {"url":"https://www.instagram.com/p/DQ1YCqlAt9D/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="}
#
# headers = {
# 	"x-rapidapi-key": instagram_api,
# 	"x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
# }
#
#
#
# response = requests.get(url, headers=headers, params=querystring)
# result = response.json()
#
# request_limit = response.headers.get("x-ratelimit-requests-remaining")
#
# media_list = []
#
# # for media in result["data"]["medias"]:
# #     if media["type"] != "audio":
# #         media_list.append(media)
#
# print(request_limit)
#
# import asyncio
# from shazamio import Shazam
#
#
# # async def main():
# #   shazam = Shazam()
# #   # out = await shazam.recognize_song('dora.ogg') # slow and deprecated, don't use this!
# #   out = await shazam.recognize('audio.mp4')
# #   result = out["track"]["url"]  # rust version, use this!
# #   print(result)
# #
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())
