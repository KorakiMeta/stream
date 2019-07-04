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
##        if len(self.playlist) < 2:
##            self.newGET()
        return PLAYLIST

##    def addGET(self):
##        self.newGET()
##        if DOWNLOAD_ALL_MODE == 0:
##            if len(self.playlist) > 3: #воткнуть в др. место
##                global HISTORY
##                HISTORY += self.playlist.pop(0)

##def test_playlist():
##    p = Playlist() #воткнуть в др. место
##    t1 = threading.Thread(target = p.newGET())
##
##test_playlist()
##print(PLAYLIST)
    
