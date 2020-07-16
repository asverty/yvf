import os

from pprint import pprint

from googleapiclient.discovery import build

key = 'AIzaSyAXfomHZwCR5cYBXBIdgv_fxZQgmgKp0yc'

youtube = build('youtube', 'v3', developerKey=key)

request = youtube.channels().list(
        part='statistics',
        forUsername='moscowdjangoru'  
    )

response = request.execute()

pprint(response)