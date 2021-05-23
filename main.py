"""
environment:
|-Python v3.8.8
|-Anaconda v4.10.1
|-Pip v21.0.1
  |-Pygame
"""
import sys
import pygame as pg
import random as rdm
# from pygame.locals import QUIT, KEYDOWN, KEYUP, K_r
# TODO sprite部分怪怪ㄉ
imgPATH = 'media/car.png'
pg.init()
winnerExist = False
font = pg.font.Font("media/Arial.ttf", 28)
clock = pg.time.Clock()
gamestatus = True


class Car(pg.sprite.Sprite):
    def __init__(self, posix):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(imgPATH)
        self.rect = self.image.get_rect()
        self.posix = posix
        self.rect.topleft = posix
        self.velocity = 0

    def findvelo(self):
        self.velocity = rdm.randrange(1, 15, 1)
        return

    def run(self):
        self.posix += self.velocity
        return

    def reset(self):
        self.posix = 0
        self.findvelo()


def paintroute():
    # 色票見：https://github.com/yen0224/NCUEHWPJ2/tree/6cff1003373e6c2a9dfc30838ab782b532c6a795
    window_surface.fill((255, 255, 255))
    # 繪製跑道
    pg.draw.rect(window_surface, (208, 219, 151), [0, 0, 800, 60])
    pg.draw.rect(window_surface, (105, 181, 120), [0, 60, 800, 60])
    pg.draw.rect(window_surface, (58, 125, 68), [0, 120, 800, 60])
    pg.draw.rect(window_surface, (37, 77, 50), [0, 180, 800, 60])
    pg.draw.rect(window_surface, (24, 29, 39), [0, 240, 800, 60])
    # 繪製終點線
    pg.draw.line(window_surface, (171, 209, 181), [720, 60], [720, 300], 2)


def paintcar():
    pg.draw.rect(window_surface, (255, 255, 255), [CarA.posix, 50, 30])
    pg.draw.rect(window_surface, (255, 255, 255), [CarB.posix, 50, 30])
    pg.draw.rect(window_surface, (255, 255, 255), [CarC.posix, 50, 30])
    pg.draw.rect(window_surface, (255, 255, 255), [CarD.posix, 50, 30])


# initialize
CarA = Car([0, 75])
CarB = Car([0, 135])
CarC = Car([0, 195])
CarD = Car([0, 255])
# set v
CarA.findvelo()
CarB.findvelo()
CarC.findvelo()
CarD.findvelo()
# test print the velocity

print(CarA.velocity, "pixel(s) per time unit")
print(CarB.velocity, "pixel(s) per time unit")
print(CarC.velocity, "pixel(s) per time unit")
print(CarD.velocity, "pixel(s) per time unit")

# 設置視窗標題為 Car Race
pg.display.set_caption('Car Race')
screen = pg.display.set_mode((800, 300))
window_surface = pg.Surface(screen.get_size())
paintroute()
paintcar()
text_surface = font.render("Press any key to start the race!!", True, (24, 29, 39))
window_surface.blit(text_surface, (0, 0))
screen.blit(window_surface, (0, 0))
pg.display.update()
# 事件迴圈監聽事件，進行事件處理
running = True
while running:
    clock.tick(60)
    KEY = pg.key.get_pressed()
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pg.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if gamestatus and [pg.K_SPACE]:
            if CarA.posix <= 720 and CarB.posix <= 720 and CarC.posix <= 720 and CarD.posix <= 720:
                CarA.run()
                CarB.run()
                CarC.run()
                CarD.run()
                text_surface = font.render('Position  [CarA]: %d [CarB]: %d [CarC]: %d [CarD]: %d'
                                           % (CarA.posix, CarB.posix, CarC.posix, CarD.posix),
                                           True, (24, 29, 39))

            else:
                text_surface = font.render("Race is end. Press R to reset and restart", True, (24, 29, 39))
                gamestatus = False

        if gamestatus is False and KEY[pg.K_r]:
            CarA.reset()
            CarB.reset()
            CarC.reset()
            CarD.reset()
            gamestatus = True

    paintroute()
    paintcar()
    # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
    window_surface.blit(text_surface, (0, 0))
    screen.blit(window_surface, (0, 0))
    pg.display.update()
