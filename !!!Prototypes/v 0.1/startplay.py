import os
import pygame
import director
import threading

PLAY = 1
NEXT = 0
NEXT_BUTTON = 0
PREV = 0
DOWN = 0
DOWNLOAD_ALL = 1 #on/off in shell


d = director.Director()
d.preDownload()
PLAYLIST = director.PLAYLIST

class Player():

    def __init__(self):
##        d = director.Director()
##        self.song = d.preDownload()
##        print(director.count[0])
        global PLAYLIST
        self.song = PLAYLIST

    def play(self):        
        if PLAY == 1:#PLAY_BUTTON = 1 (thread)
##            os_pathCWD = os.getcwd()
            pygame.mixer.init()
            pygame.mixer.music.load(os.getcwd() +
                                    '/' + 'media/' +
                                    self.song[0][-2] + '/' +
                                    self.song[0][-2] + '.mp3')
            pygame.mixer.music.play(0)#параллельно запуск таймера
            print(os.getcwd() +
                  '/' + 'media/' +
                  self.song[0][-2] + '/' +
                  self.song[0][-2] + '.mp3')
        return self

##        pygame.mixer.init()
##        pygame.mixer.music.load('D:\Py\Radio\project/media/Bluezz '
##                                'Vylez – Craters and Lovers/Bluezz'
##                                ' Vylez – Craters and Lovers.mp3')
##        pygame.mixer.music.play(0)

    def next(self):
        #if playing is end.. or NEXT_BUTTON
        
        global NEXT_BUTTON
        NEXT_BUTTON += 1
        if NEXT_BUTTON:
            pygame.mixer.init()
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.getcwd() +
                                    '/' + 'media/' +
                                    self.song[0][-1] + '/' +
                                    self.song[0][-1] + '.mp3')
            pygame.mixer.music.play(0)#параллельно запуск таймера
            print(os.getcwd() +
                                    '/' + 'media/' +
                                    self.song[0][-1] + '/' +
                                    self.song[0][-1] + '.mp3')
        threading.Thread(target = d.preDownload).start()
        return self
                
##threading.Thread(Player().play()).start()
##if self.song[4][-2]:
##    threading.Thread(Player.play()).start()
