import os

from googleapiclient.discovery import build

api_key = 'AIzaSyBSXXvCiDlURN5y7xP4DZYpJNpMbOGCTLQ'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.playlistItems().list(
        part='snippet',
        playlistId="PLv_zOGKKxVph51u_AIswuXCasZ7aZD8t3",
        maxResults='79'
)

# request1 = youtube.channels().list(
#         part='statistics',
#         forUsername='moscowdjangoru'  
#     )

response = request.execute()

# response1 = request1.execute()

for items in response['items']:    
    print(items['snippet']['title'])

# print(response)
