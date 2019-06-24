import os, shutil, requests
import playlist

CAN_PLAY = [False, False]

class Director():
    def __init__(self):
        p = playlist.Playlist()
        self.list = p.newGET()
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
        for i in range(len(self.list)):
            if not os.path.exists(self.os_path[i]):
                os.makedirs(self.os_path[i])
                if requests.get(self.MP3[i], stream = True).status_code == 200:
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
                    global CAN_PLAY
                    CAN_PLAY[i] = True
            global CAN_PLAY
            CAN_PLAY[i] = True                
        print(self.list, '\n\n',
              self.TITLE, '\n',
              self.MP3, '\n',
              self.TIME, '\n',
              self.PIC, '\n',
              self.os_path, '\n')
        
    def deleter(self):
        pass ####







        
