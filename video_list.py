import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
PLAYLIST_ID = os.getenv('PLAYLIST_ID')
video_urls = []

url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={PLAYLIST_ID}&key={API_KEY}&maxResults=50'

while url:
    response = requests.get(url)
    data = response.json()

    for item in data['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_urls.append(video_url)

    # 次のページがある場合はURLを更新
    url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={PLAYLIST_ID}&key={API_KEY}&maxResults=50&pageToken={data.get("nextPageToken", "")}' if 'nextPageToken' in data else None

# CSVに保存
with open('video_urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for url in video_urls:
        writer.writerow([url])