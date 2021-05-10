import sys
import pygame as pg
import random as rdm
from pygame.locals import QUIT
imgPATH = 'media/car.png'
pg.init()
winnerExist = False


class Car:
    def __init__(self, posix, velocity):
        self.posix = posix
        self.velocity = velocity

    def findposix(self):
        return self.posix

    def findvelo(self):
        self.velocity = rdm.randrange(10, 100, 1)
        return

    def run(self):
        self.posix += self.velocity
        return


# initialize
CarA = Car(0, 0)
CarB = Car(0, 0)
CarC = Car(0, 0)
CarD = Car(0, 0)
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
window_surface = pg.Surface([800, 640])
# 清除畫面並填滿背景色
window_surface.fill((255, 255, 255))

# 繪製跑道
pg.draw.rect(window_surface, (102, 178, 255), [0, 120, 800, 60])
pg.draw.rect(window_surface, (102, 178, 255), [0, 240, 800, 60])
pg.draw.rect(window_surface, (102, 178, 255), [0, 360, 800, 60])
pg.draw.rect(window_surface, (102, 178, 255), [0, 480, 800, 60])
# 繪製終點線
pg.draw.line(window_surface, (255, 0, 0), [760, 0], [760, 600])

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pg.display.update()

# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pg.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pg.quit()
            sys.exit()
