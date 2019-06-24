import os
import pygame

######################
#     РАБОТАЕТ!!!    #
######################

class Music(object):

    def __init__(self, song):
        self.song = song

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(0)

a = Music("D:\Py\Radio\project/media/Bluezz Vylez – Craters and Lovers/Bluezz Vylez – Craters and Lovers.mp3").play()


