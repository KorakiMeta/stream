import os, shutil, requests
import playlist

count = [1]
objPlaylist = playlist.Playlist()
objPlaylist.newGET()
PLAYLIST = objPlaylist.playlist#[]
##PLAYLIST.append(objPlaylist.playlist)

NEXT = False
CAN_PLAY = [False, False]

##objPlaylist = playlist.Playlist()
##objPlaylist.newGET()

class Director():

    def preDownload(self):# Параметр = глобальная переменная
##        objPlaylist = playlist.Playlist()
##        objPlaylist.newGET()

##        self.list = objPlaylist.playlist
        global PLAYLIST
        self.list = PLAYLIST

        global CAN_PLAY# = [False, False] #* len(objPlaylist.playlist)

        TITLE = [0, 0] #* len(objPlaylist.playlist)
        MP3 = [0, 0] #* len(objPlaylist.playlist)
        PIC = [0, 0] #* len(objPlaylist.playlist)
        duration = [0, 0] #* len(objPlaylist.playlist)
        os_path = [0, 0]
        
        
        """If first start"""
        if count[0] == 1:     
            for i in range(len(self.list)):
                os_path[i] = 'media/' + self.list[i][0]

            for i in range(len(os_path)):
                if not (os.path.exists(os_path[i])):
                    os.makedirs(os_path[i])

            #GLOBAL_LISTS
            for i in range(len(self.list)):
                TITLE[i] = self.list[i][0]#str
                MP3[i] = playlist.retrowave + self.list[i][1]#str
                PIC[i] = playlist.retrowave + self.list[i][3]#str
                duration[i] = self.list[i][2]#int

            for i in range(len(self.list)):
                if requests.get(MP3[i], stream = True).status_code == 200:
                    #PIC
                    (URLPICpath, URLPIC) = PIC[i].rsplit('/', 1)
##                    print(URLPIC)
                    with open(os_path[i] + '/' + URLPIC, 'wb') as filePIC:
                        requests.get(PIC[i], stream = True).raw.decode_content = True
                        shutil.copyfileobj(requests.get(PIC[i], stream = True).raw, filePIC)

                    #MP3
                    (URLMP3path, URLMP3) = MP3[i].rsplit('/', 1)
##                    print(URLMP3)
                    with open(os_path[i] + '/' + TITLE[i] + '.mp3', 'wb') as fileMP3:
                        requests.get(MP3[i], stream = True).raw.decode_content = True
                        shutil.copyfileobj(requests.get(MP3[i], stream = True).raw, fileMP3)
                    CAN_PLAY[i] = True
                    print(CAN_PLAY[i])

            count[0] = 666

        """If NEXT button/automaticaly is True"""
        global NEXT
        NEXT = True #пока вместо кнопки (глобальная переменная плеера)
        if NEXT == True:
            objPlaylist.addGET()
            print(self.list)
            CAN_PLAY += [False]
            TITLE += [self.list[-1][0]]
            MP3 += [playlist.retrowave + self.list[-1][1]]
            PIC += [playlist.retrowave + self.list[-1][3]]
            duration += [self.list[-1][2]]

            #PATHS
            os_path += ['media/' + self.list[-1][0]]
            for i in range(len(os_path)):
                if not (os.path.exists(os_path[-1])):
                    os.makedirs(os_path[-1])

            if requests.get(MP3[-1], stream = True).status_code == 200:
                #PIC
                (URLPICpath, URLPIC) = PIC[-1].rsplit('/', 1)
##                print(URLPIC)
                with open(os_path[-1] + '/' + URLPIC, 'wb') as filePIC:
                    requests.get(PIC[-1], stream = True).raw.decode_content = True
                    shutil.copyfileobj(requests.get(PIC[-1], stream = True).raw, filePIC)

                #MP3
                (URLMP3path, URLMP3) = MP3[-1].rsplit('/', 1)
##                print(URLMP3)
                with open(os_path[-1] + '/' + TITLE[-1] + '.mp3', 'wb') as fileMP3:
                    requests.get(MP3[-1], stream = True).raw.decode_content = True
                    shutil.copyfileobj(requests.get(MP3[-1], stream = True).raw, fileMP3)
                CAN_PLAY[-1] = True
                print(CAN_PLAY[-1])

            
##        print(TITLE, MP3, PIC, duration, CAN_PLAY, os_path)
        PLAYLIST = [TITLE, MP3, PIC, duration, CAN_PLAY, os_path]
        return PLAYLIST
##        return [TITLE, MP3, PIC, duration, CAN_PLAY, os_path]

#FOR TESTING
##a=Director()
##a.preDownload()
##b=Director()
##b.preDownload()
##if a.preDownload() is b.preDownload(): #ссылка на один и тот же объект =(
##    print(count[0])
print(PLAYLIST)



