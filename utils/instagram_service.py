import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

instagram_api = os.getenv("INSTAGRAM_API")

def downloader(link):
    url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"

    querystring = {"url": link}
    
    headers = {
	"x-rapidapi-key": instagram_api,
	"x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response.text)

    
    media_list = []

    if "error" in result:
        return "error"
    else:
        for media in result["data"]["medias"]:
            if media["type"] != "audio":
                media_list.append(
                    {
                        "type": media["type"],
                        "media": media["url"]
                    }
                )
                
                

    return media_list
        


