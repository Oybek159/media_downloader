import requests

url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"

querystring = {"url":"https://www.instagram.com/reel/DJg8Hc_zkot/?igsh=MXFvaDhueHozZjQ2bQ=="}

headers = {
	"x-rapidapi-key": "5db0d31fe1msh85c3775ca6b9816p1c90a9jsn4663e78d83d8",
	"x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())