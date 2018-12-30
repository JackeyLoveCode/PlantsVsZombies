'''程序入口'''
import pygame,sys
from pygame.locals import *
from src.Peashooter import Peashooter
from src.Bullet import Bullet
from src.Zombie import Zombie
from src.SunFlower import SunFlower
from src.Sun import Sun
from src.WallNut import WallNut
pygame.init()
bg_size = (1200,600)
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("植物大战僵尸")
background_image_path = "../material/images/background1.jpg"
sunback_imgage_path = "../material/images/SunBack.png"
background = pygame.image.load(background_image_path).convert()
sunback = pygame.image.load(sunback_imgage_path).convert()
#创建豌豆射手对象
peashooter = Peashooter(bg_size)
#创建僵尸对象
zombie = Zombie(bg_size)
#创建太阳花对象
sunFlower = SunFlower(bg_size)
#创建太阳对象
#sun = Sun(sunFlower.rect,bg_size)
#创建坚果对象
wallNut = WallNut(bg_size)
# font = pygame.font.Font("totalSuns",1024)
# totalSuns = font.render(100,True,(255,255,255),None)
#定义生成太阳的事件
GENERATORSUNEVNET = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATORSUNEVNET,5000)
# 创建太阳数量文本
text = "950"
suns_font = pygame.font.SysFont("arial", 25)
suns_number_surface = suns_font.render(text, True, (0, 0, 0), (255, 255, 255))


def main():
    #声明太阳数量为全局变量
    global text
    global suns_number_surface
    global suns_font
    running = True
    delay = 60
    # 生成子弹
    bulls = pygame.sprite.Group()
    #生成太阳
    suns = pygame.sprite.Group()
    while running:
        delay -= 1
        if delay == 0:
            delay = 60
        # 绘制背景
        screen.blit(background,(0,0))
        #绘制顶部太阳数量栏
        screen.blit(sunback,(250,0))
        screen.blit(suns_number_surface,(300,3))
        clock = pygame.time.Clock()
        clock.tick(20)
        #绘制豌豆射手
        if  peashooter.active:
            screen.blit(peashooter.images[delay % 13],peashooter.rect)
        # 绘制太阳花
        if sunFlower.active:
            screen.blit(sunFlower.images[delay % 13], sunFlower.rect)
        #绘制坚果对象
        if wallNut.active:
            screen.blit(wallNut.images[delay % 13],wallNut.rect)
        # 绘制太阳
        # if delay % 10 == 0:
        #     sun = Sun(sunFlower.rect, bg_size)
        #     suns.add(sun)
        # suns.update()
        # suns.draw(screen)

        #绘制僵尸
        if zombie.active:
            screen.blit(zombie.images[delay % 21],zombie.rect)
            zombie.move()
        # 子弹
        if delay % 30 == 0:
            bul = Bullet(peashooter.rect, bg_size)
            bulls.add(bul)
        bulls.update()
        bulls.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #生成太阳
            if event.type == GENERATORSUNEVNET:
                sun = Sun(sunFlower.rect,bg_size)
                suns.add(sun)
                print(suns.__len__())
            if event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                print(pressed_array)
                if pressed_array[0]:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    if x <= sun.rect.left + sun.rect.width and y <= sun.rect.top + sun.rect.height:
                        if sun.active:
                            #sun.active = False
                            suns.remove(sun)
                            text = str(int(text) + 50)
                            suns_font = pygame.font.SysFont("arial", 25)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0), (255, 255, 255))
                            screen.blit(suns_number_surface, (300, 3))
        for sun in suns:
            if sun.active:
                screen.blit(sun.image,sun.rect)
        pygame.display.update()
if __name__ == '__main__':
    main()