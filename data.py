from pytube import YouTube
import pandas as pd
import csv

video_list = pd.read_csv("video_urls.csv", header=None).values.tolist()

print(video_list)

video_informations = []

for url in video_list:
    try:
        yt = YouTube(url[0])
        information = (yt.title, yt.publish_date, yt.description)
        video_informations.append(information)
        print(f"Title: {yt.title}")
        print(f"published: {yt.publish_date}")
        print(f"description: {yt.description}")
    except Exception as e:
        print(f"エラー: {url[0]} - {e}")

with open('video_informations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for info in video_informations:
        writer.writerow([info[0], info[1], info[2]])