import os
import shutil
import requests
import threading
import playlist

RUN = False
CAN_PLAY = []
HISTORY = []

class Director:
       
    def __init__(self):
        """init method, also update"""
        p = playlist.Playlist()
        p.newGET()    
        self.list = playlist.PLAYLIST
        self.TITLE = []
        self.MP3 = []
        self.TIME = []
        self.PIC = []
        self.os_path = []
        for i in range(len(self.list)):                     
            self.TITLE += [self.list[i][0]]
            self.MP3 += [playlist.retrowave + self.list[i][1]]
            self.TIME += [self.list[i][2]]
            self.PIC += [playlist.retrowave + self.list[i][3]]
            self.os_path += ['media/' + self.list[i][0]]
                
    def preDownload(self):
        """Predownloading for playing"""
##        if len(self.list) < 2:
##            Director().__init__()
        for i in range(len(self.list)):
            if not os.path.exists(self.os_path[i]) and requests.get(self.MP3[i], stream = True).status_code == 200:
                """Creates new directory"""
                os.makedirs(self.os_path[i])
            
                """DOWNLOAD PIC"""
                (URLPICpath, URLPIC) = self.PIC[i].rsplit('/', 1)
                with open(self.os_path[i] + '/' + URLPIC, 'wb') as filePIC:
                    requests.get(self.PIC[i],
                                 stream = True).raw.decode_content = True
                    shutil.copyfileobj(requests.get(self.PIC[i],
                                                    stream = True).raw,
                                       filePIC)
                
                """DOWNLOAD MP3"""
                (URLMP3path, URLMP3) = self.MP3[i].rsplit('/', 1)
                with open(self.os_path[i] + '/' + self.TITLE[i] + '.mp3', 'wb') as fileMP3:
                    requests.get(self.MP3[i], stream = True).raw.decode_content = True
                    shutil.copyfileobj(requests.get(self.MP3[i], stream = True).raw, fileMP3)               
        print(self.list, '\n\n',
              self.TITLE, '\n',
              self.MP3, '\n',
              self.TIME, '\n',
              self.PIC, '\n',
              self.os_path, '\n')
##            if len(self.list) > 3:
##                global HISTORY
##                HISTORY += self.list.pop(0)

    def update(self):
        p = playlist.Playlist()
        self.list += p.newGET()
        
        
    def deleter(self):
        pass







        
