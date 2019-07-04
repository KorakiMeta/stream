import os
import time
import pygame
import playlist
import director

PLAYING = False
POS = -2

class Player():

    def __init__(self):
        pygame.mixer.init()
        d = director.Director()
        d.preDownload()
        self.song = d.list
        self.TITLE = []
        self.MP3 = []
        self.TIME = []
        self.PIC = []
        if len(self.song) < 2:
            self.__init__()
        for i in range(len(self.song)):                     
            self.TITLE += [self.song[i][0]]
            self.MP3 += [playlist.retrowave + self.song[i][1]]
            self.TIME += [self.song[i][2]]
            self.PIC += [playlist.retrowave + self.song[i][3]]

    def play(self, POS):
        pygame.mixer.music.load(os.getcwd() +
                                '/' + 'media' + '/' +
                                self.TITLE[POS] + '/' + self.TITLE[POS] + '.mp3')
        pygame.mixer.music.play()
        print(self.TITLE[POS])

    def pause(self):
        pygame.mixer.music.pause()

    def new_song(self):
        time.sleep(1)
        self.play(POS)
        self.__init__()
        
    def prev_song(self):
        time.sleep(1)
        global POS
        POS -= 1
        assert POS < 0
        if (-POS) > len(self.TITLE):
            POS += 1
        self.play(POS)

    def next_song(self):
        time.sleep(1)
        global POS
        POS += 1
        assert POS <= 0
        if POS >= (-1):
            self.new_song()
            POS -= 1
        else:    
            self.play(POS)
        
        
        
