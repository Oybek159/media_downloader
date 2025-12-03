import requests

url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"

querystring = {"url":"https://www.instagram.com/p/DQ1YCqlAt9D/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="}

headers = {
	"x-rapidapi-key": "5db0d31fe1msh85c3775ca6b9816p1c90a9jsn4663e78d83d8",
	"x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
result = response.json()

media_list = []

for media in result["data"]["medias"]:
    if media["type"] != "audio":
        media_list.append(media)

print(media_list)