# 彰化師大機電系第二次實做作業（version 1.0）
---
## TODO
車子改為圖片插入 
結束動畫 
status bar
## 程式內容說明
### 使用套件：
| 套件名/程式名 | 版本 | 附註 |
| :---: | :---: | :---:|
|python|v3.8.8|Anaconda env|
|pygame|2.0.1|*需安裝*|
|random|N/A|亂數|
|sys|N/A|系統|
### 分段說明
#### 引入必要之函式庫、仔入相關定義、路徑
```python
import sys
import pygame as pg
import random as rdm
from pygame.locals import QUIT, KEYDOWN, KEYUP
imgPATH = 'media/car.png'
pg.init()
winnerExist = False
font = pg.font.Font("media/Arial.ttf", 28)
clock = pg.time.Clock()
```
附註：安裝套件方法
````
pip install [package name]
或
conda install [package name]
````
#### 定義class類別
* 設置初始位置、初始速度（先定為零）
* 定義class method
* *findvelo* :取亂數種子，並將其賦予velocity變數儲存
* *run*:遞增位置
````python
class Car:
    def __init__(self, posix, velocity):
        self.posix = posix
        self.velocity = velocity

    def findvelo(self):
        self.velocity = rdm.randrange(1, 15, 1)
        return

    def run(self):
        self.posix += self.velocity
        return

````

#### 繪圖部分
````python
def paintroute():
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
    pg.draw.rect(window_surface, (255, 255, 255), [CarA.posix, 75, 50, 30])
    pg.draw.rect(window_surface, (255, 255, 255), [CarB.posix, 135, 50, 30])
    pg.draw.rect(window_surface, (255, 255, 255), [CarC.posix, 195, 50, 30])
    pg.draw.rect(window_surface, (255, 255, 255), [CarD.posix, 255, 50, 30])
````
繪圖語法：
````python
# 長方形
pygame.draw.rect(surface_Name,(*rgb* color), [Ｘ座標, Ｙ座標, 長方形之長, 長方形之寬])
# 畫線
pygame.draw.line(surface_Name,(*rgb* color),[起始座標],[終點座標])
````
````python
# initialize
CarA = Car(0, 0)
CarB = Car(0, 0)
CarC = Car(0, 0)
CarD = Car(0, 0)
pg.display.set_caption('Car Race')
screen = pg.display.set_mode((800, 300))
window_surface = pg.Surface(screen.get_size())
paintroute()
paintcar()
text_surface = font.render("Press [> SPACE <] to start the race!!", True, (24, 29, 39))
window_surface.blit(text_surface, (0, 0))
screen.blit(window_surface, (0, 0))
pg.display.update()
````
````python
running = True
while running:
    clock.tick(60)
    KEY = pg.key.get_pressed()
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pg.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        paintroute()
        if KEY[pg.K_SPACE]:
            if CarA.posix <= 720 and CarB.posix <= 720 and CarC.posix <= 720 and CarD.posix <= 720:
                CarA.run()
                CarB.run()
                CarC.run()
                CarD.run()
                text_surface = font.render('Position  [CarA]: %d [CarB]: %d [CarC]: %d [CarD]: %d'
                                           % (CarA.posix, CarB.posix, CarC.posix, CarD.posix),
                                           True, (24, 29, 39))
                paintcar()

            else:
                paintcar()
                text_surface = font.render("Race is end.", True, (24, 29, 39))
            # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
            window_surface.blit(text_surface, (0, 0))
            screen.blit(window_surface, (0, 0))
            pg.display.update()

````
# To Be Continue