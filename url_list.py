import requests
import json

api_key = ''
channel_id = ''
    
    
def fetch_all_urls(channel_id):
    """ Get all video urls from a youtube channel """

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = requests.get(url)
        resp = json.loads(inp.text)
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append([i['snippet']['title'], base_video_url + i['id']['videoId']])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links
    
    
with open('urls-title.txt','a') as f:
    for i in fetch_all_urls(channel_id):
        f.write(i[0] + " - " + i[1])
        f.write('\n')