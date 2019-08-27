import os
import asyncio
import pygame
import playlist
import director
import player

Color = {'WHITE'      : (255, 255, 255), \
          'BLACK'      : (0, 0, 0),       \
          'GRAY'       : (30, 32, 30),    \
          'DARKGRAY'   : (15, 17, 15),    \
          'GRAY'       : (30, 31, 30),    \
          'DARKGRAY'   : (15, 15, 15),    \
          'COPPER'     : (163, 141, 109), \
          'DARKCOPPER' : (143, 121, 89)}

GUIButtons = (('prev.bmp','prev.bmp'),
              ('play.bmp','pause.bmp'),
              ('next.bmp','next.bmp'))

run = True
direct = os.getcwd() + '/media/'
sources = os.getcwd() + '/sources/'
       
class Button(player.Player):

    def __init__(self, width_i = 60, height_i = 60,
                 prev_x = 100, play_x = 300, next_x = 500, but_y = 550):
        
        super().__init__()
         
        self.TITLE_text = self.TITLE[self.POS]
        self.TIME_text_m = self.TIME[self.POS]/1000//60
        self.TIME_text_s = self.TIME[self.POS]/1000%60//60

        self.prev_x = prev_x
        self.play_x = play_x
        self.next_x = next_x
        self.but_y = but_y
        self.but_x = (prev_x, play_x, next_x)

        self.width = width_i
        self.height = height_i

    def play(self):
        super().play()
        self.IMG_preload()
        """добавить воспроизведение таймера"""

    def next_song(self):
        super().next_song()

    def prev_song(self):
        super().prev_song()
        self.IMG_preload()


    def IMG_preload(self):
        self.img = pygame.image.load(self.IMG[self.POS]).convert()
        """Вписать в стандартный размер - OK"""
        scale = pygame.transform.scale(self.img, (self.img.get_width()*300//self.img.get_width(),
                                                  self.img.get_height()*300//self.img.get_width()))
        scale_rect = scale.get_rect(center = (300, 200))
        screen.blit(scale, scale_rect)

    def draw(self, outline = None):
        self.color = Color['GRAY']
        for x in self.but_x:
            pygame.draw.rect(screen, self.color, (x - 30, self.but_y - 30, self.width,
                                                  self.height), 0)
        for i in range(len(GUIButtons)):
            if self.PLAYING:
                self.img_but = pygame.image.load(sources + GUIButtons[i][1]).convert()
                scale_img_but = pygame.transform.scale(self.img_but, (self.img_but.get_width()//10,
                                                                      self.img_but.get_height()//10))
                scale_rect = scale_img_but.get_rect(center = (self.but_x[i], self.but_y))
                screen.blit(scale_img_but, scale_rect)
                continue
            else:
                self.img_but = pygame.image.load(sources + GUIButtons[i][0]).convert()
                scale_img_but = pygame.transform.scale(self.img_but, (self.img_but.get_width() // 10,
                                                                      self.img_but.get_height() // 10))
                scale_rect = scale_img_but.get_rect(center = (self.but_x[i], self.but_y))
                screen.blit(scale_img_but, scale_rect)
                continue

        """TITLE"""
        font = pygame.font.SysFont('comicsans', 25)
        text = font.render(self.TITLE[self.POS], 1, (255, 255, 255))
        screen.blit(text, (self.play_x - text.get_width()//2, 380))

        """TIME_of_PLAYING"""
        font = pygame.font.SysFont('comicsans', 25)
        text_time = font.render('/ ' + self.TIMER[self.POS], 1, (255, 255, 255))
        screen.blit(text_time, (self.play_x, 425))
        

    async def Timer(self):
        """ Пока не работает. Неприятности с корутиной внутри "синхронного класса".
        Больная логика больного ума при вызове event loop из event loop lol. Исправить! """
        self.M = 0
        self.S = 0
        self.time = '{0}:{1}'

        async def go():
            while self.PLAYING:
                await asyncio.sleep(1)
                self.S += 1
                if self.S == 60:
                    self.M += 1
                    self.S = 0
                await print_time()
                continue
        
        async def print_time():
            if self.S < 10:
                self.time = '{0}:0{1}'
            TS = self.time.format(self.M, self.S)
            font = pygame.font.SysFont('comicsans', 36)
            text_time = font.render(TS, 1, (128, 210, 230))
            screen.blit(text_time, (self.play_x - 60, 420))

        async def main():
            task = asyncio.create_task(go())
            await asyncio.gather(task)

        await main()

    def isOver_prev(self, mouse_pos):
        if mouse_pos[0] > self.prev_x - 32 and mouse_pos[0] < self.prev_x + 32:
            if mouse_pos[1] > self.but_y - 32 and mouse_pos[1] < self.but_y + 32:
                return True
        return False
    
    def isOver_play(self, mouse_pos):
        if mouse_pos[0] > self.play_x - 32 and mouse_pos[0] < self.play_x + 32:
            if mouse_pos[1] > self.but_y - 32 and mouse_pos[1] < self.but_y + 32:
                return True
        return False
    
    def isOver_next(self, mouse_pos):
        if mouse_pos[0] > self.next_x - 32 and mouse_pos[0] < self.next_x + 32:
            if mouse_pos[1] > self.but_y - 32 and mouse_pos[1] < self.but_y + 32:
                return True
        return False



panel = Button()
while run:
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((0, 0, 0))
    panel.draw()
    panel.IMG_preload()
    pygame.display.update()
    
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if panel.isOver_prev(mouse_pos):
                panel.prev_song()
                print(panel.POS)
                continue
        else:
            continue
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if panel.isOver_play(mouse_pos) and panel.PLAYING == False:
                panel.play()
                print(panel.POS)
                continue
            elif panel.isOver_play(mouse_pos) and panel.PLAYING == True:
                panel.pause()
                continue
        else:
            continue
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if panel.isOver_next(mouse_pos):
                panel.pause()
                panel.next_song()
                print(panel.POS)
                continue
        else:
            continue           