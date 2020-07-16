import os

from pprint import pprint

from googleapiclient.discovery import build

key = 'SECTRET_KEY'

youtube = build('youtube', 'v3', developerKey=key)

request_1 = youtube.playlistItems().list(
        part='snippet',
        playlistId="PLv_zOGKKxVph51u_AIswuXCasZ7aZD8t3",
        maxResults='50'
)

request_2 = youtube.playlistItems().list(
        part='snippet',
        playlistId="PLv_zOGKKxVph51u_AIswuXCasZ7aZD8t3",
        maxResults='50',
        pageToken='CDIQAA'
)

response_1 = request_1.execute()

for items in response_1['items']:    
    pprint(items['snippet']['title'])

response_2 = request_2.execute()

for items in response_2['items']:    
    pprint(items['snippet']['title'])
