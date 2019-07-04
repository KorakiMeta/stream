import os
import time
import pygame
import playlist
import director
import player

PLAYING = False
POS = -2
run = True
direct = os.getcwd() + '/media/'
size = width, height = (700, 700)
screen = pygame.display.set_mode(size)
##pygame.init()

class GUI(player.Player):

    def __init__(self):
        super().__init__()
        for i in range(len(self.song)):
            artwork = self.song[i][0] + self.song[i][3].replace('/artwork', '')
            self.PIC += [direct + artwork]

        global run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    def play(self, POS):
        self.IMG = pygame.image.load(self.PIC[player.POS])
        screen.blit(self.IMG, (0, 0))
        super().play(POS)
        
        
