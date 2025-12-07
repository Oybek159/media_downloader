import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# instagram_api = os.getenv("INSTAGRAM_API")
# second_instagram_api = os.getenv("SECOND_INSTAGRAM_API")
#
# api_keys = [instagram_api, second_instagram_api]


def downloader(link):
    media_list = []
    audio_list = []

    # API request code (commented out for testing)
    # url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"
    # querystring = {"url": link}
    # for api_key in api_keys:
    #     headers = {
    #         "x-rapidapi-key": api_key,
    #         "x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
    #     }
    #     response = requests.get(url, headers=headers, params=querystring)
    #     remaining_limit = int(response.headers.get("x-ratelimit-requests-remaining", 0))
    #     print(remaining_limit)
    #     if remaining_limit == 0:
    #         print("Switched api key...")
    #         continue
    #     result = json.loads(response.text)
    #     print(result)
    #     print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #     if "error" in result:
    #         return "error"
    #     else:
    #         for media in result.get("data", {}).get("medias", []):
    #             if media["type"] != "audio":
    #                 media_list.append(
    #                     {
    #                         "type": media["type"],
    #                         "media": media["url"]
    #                     }
    #                 )
    #             elif media["type"] == "audio":
    #                 audio_list.append(
    #                     {
    #                         "type": media["type"],
    #                         "audio": media["url"]
    #                     }
    #                 )
    #         break

    # Load data from local JSON file for testing
    json_path = os.path.join(os.path.dirname(__file__), "instagram.json")
    with open(json_path, "r") as file:
        result = json.load(file)

    if "error" in result:
        return "error"
    else:
        for media in result.get("data", {}).get("medias", []):
            if media["type"] != "audio":
                media_list.append(
                    {
                        "type": media["type"],
                        "media": media["url"]
                    }
                )
            elif media["type"] == "audio":
                audio_list.append(
                    {
                        "type": media["type"],
                        "audio": media["url"]
                    }
                )

    return media_list, audio_list