import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

instagram_api = os.getenv("INSTAGRAM_API")

def insta_downloader(link):
    url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"

    querystring = {"url": link}
    
    headers = {
	"x-rapidapi-key": instagram_api,
	"x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response)

    dict = {}

    if "error" in result:
        return "error"
    else:
        if result["Type"] == "Post-Image":
            dict["type"] = "image"
            dict["media"] = result["media"]
            return dict
        elif result["Type"] == "Post-Video":
            dict["type"] = "video"
            dict["media"] = result["media"]
            return dict
        elif result["Type"] == "Carousel":
            dict["type"] = "carousel"
            dict["media"] = result["media"]
            return dict
