from googleapiclient.discovery import build
import pandas as pd
import gspread
import df2gspread as d2g
import config

key = config.YOUTUBE_API_KEY

playlist_id = config.PLAYLIST_ID

youtube = build("youtube", "v3", developerKey=key)

def get_playlist_videos(playlist_id):
    videos = []
    res = youtube.playlistItems().list(playlistId=playlist_id, 
                                       part='snippet', 
                                       maxResults=50,
                                      ).execute()
    videos += res['items']

    next_page_token = 'CDIQAA'

    if next_page_token is next_page_token:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
    videos += res['items']
    next_page_token = res.get('nextPageToken')

    return videos

videos = get_playlist_videos(playlist_id)


def get_videos_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(id=','.join(video_ids[i:i+50]),
                                part='statistics').execute()
        stats += res['items']

    return stats

video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))

stats = get_videos_stats(video_ids)

d = []
if len(stats)!=len(videos):
    i=1
    j=0
else:
    i=0
    j=0
len_video = len(videos)
len_stats = len(stats)
for video in videos:
    if i >= len_video:
        break
    Url_video='https://www.youtube.com/watch?v='+videos[i]['snippet']['resourceId']['videoId']
    d.append((videos[i]['snippet']['publishedAt'],
              videos[i]['snippet']['title'],
              videos[i]['snippet']['resourceId']['videoId'],
              Url_video,
              stats[j]['statistics']['viewCount'],
              stats[j]['statistics']['likeCount'],
              stats[j]['statistics']['dislikeCount']
            ))

    i+=1
    j+=1

df=pd.DataFrame(d, columns=('Published', 
                            'Title_video', 
                            'ID_video', 
                            'Url_video', 
                            'Views', 
                            'Likes', 
                            'Dislikes'
                            )
                )
df['Published'] = df['Published'].astype(str)
df['Views'] = df['Views'].astype(int)
df['Likes'] = df['Likes'].astype(int)
df['Dislikes'] = df['Dislikes'].astype(int)
df.index+=1

# spreadsheet_ID = config.SPREADSHEET_ID
# wks_name = 'YTdata'
# d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)

df.to_csv('mp.csv')
