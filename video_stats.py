import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = os.getenv("CHANNEL_HANDLE")

def get_playlist_id():
    try:
        url = "https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}".format(CHANNEL_HANDLE=CHANNEL_HANDLE, API_KEY=API_KEY)
        response = requests.get(url)
        data =response.json()
        channel_items=data.get("items", [0])
        channel_playlistID=channel_items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
        print("channel_playlistID: ", channel_playlistID)
        return channel_playlistID
    except requests.exceptions.RequestException as e: 
        raise e 

if __name__== "__main__":
    print("get playlist will be executed")
    get_playlist_id()
else:
    print("get playlist will not be executed")
        