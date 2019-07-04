import time
import os
import pygame
import playlist
import player

run = True
direct = os.getcwd() + '/media/'
size = width, height = (700, 700)
screen = pygame.display.set_mode(size)
pygame.init()

class GUI():

    def __init__(self):
##        p = player.Player()
        self.p = player
        self.PLAYER = player.Player()
##        self.list = p.song
        self.list = self.PLAYER.song
        self.TITLE = []
        self.MP3 = []
        self.TIME = []
        self.PIC = []

        for i in range(len(self.list)):                     
            self.TITLE += [self.list[i][0]]
            self.MP3 += [playlist.retrowave + self.list[i][1]]
            self.TIME += [self.list[i][2]]
            artwork = self.list[i][0] + self.list[i][3].replace('/artwork', '')
            self.PIC += [direct + artwork]

##        for i in range(len(self.PLAYER)):                     
##            self.TITLE += [self.PLAYER[i][0]]
##            self.MP3 += [playlist.retrowave + self.PLAYER[i][1]]
##            self.TIME += [self.PLAYER[i][2]]
##            artwork = self.PLAYER[i][0] + self.PLAYER[i][3].replace('/artwork', '')
##            self.PIC += [direct + artwork]

##        

##        while pygame.event.wait().type != pygame.QUIT:
##            pygame.display.flip()
##
##        pygame.quit()

        global run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    def GUI_preload_img(self):
        self.IMG = pygame.image.load(self.PIC[self.p.POS])
        screen.blit(self.IMG, (0, 0))
            

##while pygame.event.wait().type != pygame.QUIT:
##    pygame.display.flip()
##
##pygame.quit()
