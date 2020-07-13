
from googleapiclient.discovery import build

api_key = 'SECRET_KEY'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='moscowdjangoru'  
    )

response = request.execute()

print(response)
