import pandas as pd
import csv
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

video_list = pd.read_csv("video_urls.csv", header=None)[0].tolist()
video_ids = [url.split('v=')[-1] for url in video_list if 'v=' in url]

video_informations = []

# 50本ずつ分割してAPIリクエスト
for i in range(0, len(video_ids), 50):
    ids = ','.join(video_ids[i:i+50])
    api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ids}&key={API_KEY}"
    response = requests.get(api_url)
    data = response.json()
    for item in data.get('items', []):
        snippet = item['snippet']
        title = snippet.get('title', '')
        published = snippet.get('publishedAt', '')
        description = snippet.get('description', '')
        video_informations.append((title, published, description))
        print(f"Title: {title}")
        print(f"published: {published}")
        print(f"description: {description}")

with open('video_informations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for info in video_informations:
        writer.writerow([info[0], info[1], info[2]])