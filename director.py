import os
import shutil
import requests
# import threading mb aiofiles?
import playlist

RUN = False
CAN_PLAY = []
direct = os.getcwd() + '/media/'

class Director:
    """ Downloads from server """
       
    def __init__(self):
        p = playlist.Playlist()
        p.newGET()    
        self.list = playlist.PLAYLIST
        self.TITLE = []
        self.MP3 = []
        self.TIME = []
        self.PIC = []
        self.IMG = []
        self.os_path = []
        self.TIMER = []
        for i in range(len(self.list)):                     
            self.TITLE += [self.list[i][0]]
            self.MP3 += [playlist.retrowave + self.list[i][1]]
            self.TIME += [self.list[i][2]]
            M = int(self.list[i][2] / 1000 // 60) #если что, здесь возможна погрешность
            S = int((self.list[i][2] / 1000) - (self.list[i][2] / 1000 // 60) * 60)
            if S < 10:
                T = '{0}:0{1}'.format(M, S)
            else:
                T = '{0}:{1}'.format(M, S)
            self.TIMER += [T]
            self.PIC += [playlist.retrowave + self.list[i][3]]
            artwork = self.list[i][0] + self.list[i][3].replace('/artwork', '')
            self.IMG += [direct + artwork]
            self.os_path += ['media/' + self.list[i][0]]
                
    def preDownload(self):
        """Predownloading for playing"""

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
              self.IMG, '\n',
              self.os_path, '\n')
      
    def deleter(self):
        pass