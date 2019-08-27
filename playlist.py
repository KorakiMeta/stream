import os
import requests
import shutil
import json
import threading
import time

retrowave = 'https://retrowave.ru'
if not os.path.exists(os.getcwd() + '/media'):
    media = os.makedirs(os.getcwd() + '/media')
PLAYLIST = []
HISTORY = []
DOWNLOAD_ALL_MODE = 0

class Playlist:
    """ Class makes GET => JSON => list """

    def __init__(self):
        global PLAYLIST
        self.playlist = PLAYLIST

    def newGET(self, apiURL = 'https://retrowave.ru/api/v1/tracks?cursor=1&limit=1'):       
        GET = requests.get(apiURL)
        DATA = GET.json()
        title = str(DATA['body']['tracks'][0]['title']).strip()

        np = ["?", "\"", "\\", "<", ">", ":", "|", "/",]
        a = []
        for i in range(len(title)):
            if title[i] in np:
                a.append(title[i])
        for n in a:
            title = title.replace(n, "")
        
        audio = str(DATA['body']['tracks'][0]['streamUrl']).strip()
        duration = DATA['body']['tracks'][0]['duration']
        pic = str(DATA['body']['tracks'][0]['artworkUrl']).strip()
        stack = (title, audio, duration, pic)
        self.playlist.append(stack)

        return PLAYLIST