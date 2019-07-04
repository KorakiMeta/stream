import os
import time
import pygame
import playlist
import director
import player

Colour = {'WHITE'      : (255, 255, 255), \
          'BLACK'      : (0, 0, 0),       \
          'GRAY'       : (30, 32, 30),    \
          'DARKGRAY'   : (15, 17, 15),    \
          'GRAY'       : (30, 31, 30),    \
          'DARKGRAY'   : (15, 15, 15),    \
          'COPPER'     : (163, 141, 109), \
          'DARKCOPPER' : (143, 121, 89)}

GUIButtons = {'PLAY' : 'play.bmp',
              'PAUSE' : 'pause.bmp',
              'NEXT' : 'next.bmp',
              'PREV' : 'prev.bmp',
              }

PLAYING = False
run = True
direct = os.getcwd() + '/media/'
sources = os.getcwd() + '/sources/'

##size = width, height = (600, 600)
##screen = pygame.display.set_mode(size)
##win = pygame.display.set_mode((600, 600))
##win.fill((0,0,0))
##screen.fill((0, 0, 0))
##for event in pygame.event.get():
##    if event.type == pygame.QUIT:
##        run = False

##pygame.init()

class Button(player.Player):

    def __init__(self, width_i = 60, height_i = 60):
        #information self.list
        super().__init__()
        self.TITLE_text = self.TITLE[self.POS]
        self.TIME_text_m = self.TIME[self.POS]//1000
        self.TIME_text_s = self.TIME[self.POS]%1000

##        self.x = x
##        self.y = y
##        self.width = width_i
##        self.height = height_i
        
        self.x_play = 300
        self.x_next = 500
        self.x_prev = 100
        self.y = 550
        self.width = width_i
        self.height = height_i

    def draw(self, outline = None):#, key):
##        600 * 600 => 60 * 60
        if outline:
            self.button_play = pygame.draw.rect(win, outline, (self.x_play - 32, self.y - 32,
                                           self.width + 4, self.height + 4), 255)

        self.img_play = pygame.image.load(sources + GUIButtons['PLAY']).convert()
        scale_play = pygame.transform.scale(self.img_play, (self.img_play.get_width()//10,
                                                  self.img_play.get_height()//10))
        scale_rect = scale_play.get_rect(center = (300, 550))
        screen.blit(scale_play, scale_rect)

        pygame.display.update()

    def isOver(self, mouse_pos):
        if mouse_pos[0] > self.x_play - 32 and mouse_pos[0] > self.x_play + 32:
            if mouse_pos[1] > self.y - 32 and mouse_pos[1] < self.y + 32:
                return True
        return False

    def text(self):
        pass

    def timer(self):
        pass


















PLAY_button = Button()
while run:
    screen = pygame.display.set_mode((600, 600))
    screen.fill((0, 0, 0))
    PLAY_button.draw()
    pygame.display.update()
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_button.isOver(mouse_pos):
                PLAY_button.play()


        



















        
##        for i in range(len(self.list)):
##            artwork = self.list[i][0] + self.list[i][3].replace('/artwork', '')
##            self.PIC += [direct + artwork]

##        self.size = width, height = (400, 400)
##        self.screen = pygame.display.set_mode(self.size)
##
##        global run
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                run = False

    def IMG_preload(self):
        self.img = pygame.image.load(self.IMG[self.POS]).convert()
        scale = pygame.transform.scale(self.img, (self.img.get_width()//2,
                                                  self.img.get_height()//2))
        scale_rect = scale.get_rect(center = (200, 200))
        screen.blit(scale, scale_rect)
        pygame.display.update()

class Buttons:
    def __init__(self):
        source = 'D:/Py/Radio/project/sources/'
        global PLAYING
        if not PLAYING:
            self.play_img = pygame.image.load(source + 'play.bmp')
            self.play_img_rect = self.play_img.get_rect((width//2, 450))
                                                                
            screen.blit(delf.play_img, self.play_img_rect)
            pygame.display.update()
        


        
##        screen.blit(self.img, (0, 0))
##        pygame.display.update()

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True            
        return False

        
        
