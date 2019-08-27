import os
import time
import pygame
import playlist
import director

class Player(director.Director):

    def __init__(self):
        super().__init__()
        self.POS = -2
        self.PLAYING = False
        pygame.mixer.init()
        self.preDownload()

        if len(self.list) < 2:
            self.__init__()       

    def play(self):
        pygame.mixer.music.load(os.getcwd() +
                                '/' + 'media' + '/' +
                                self.TITLE[self.POS] + '/' + self.TITLE[self.POS] + '.mp3')
        pygame.mixer.music.play()
        self.PLAYING = True
        print(self.TITLE[self.POS])

    def pause(self):
        pygame.mixer.music.pause()
        self.PLAYING = False

    def new_song(self):
        self.pause()
##        time.sleep(1)
        self.__init__()
        self.play()
        
    def prev_song(self):
        self.pause()
##        time.sleep(1)
        self.POS -= 1
        assert self.POS < 0
        if -(self.POS) > len(self.TITLE):
            self.POS += 1
        self.play()

    def next_song(self):
        self.pause()
##        time.sleep(1)
        self.POS += 1
        assert self.POS <= 0
        if self.POS >= (-1):
            self.new_song()
        else:
            self.play()
        
        
        
