'''太阳花'''
import pygame


class SunFlower(pygame.sprite.Sprite):
    def __init__(self,rect,bg_size):
        super(SunFlower, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #图片
        self.image = pygame.image.load("../material/images/SunFlower_00.png")
        # 获取图片位置
        self.rect = self.image.get_rect()
        # 定义太阳花的初始化位置
        self.rect.left, self.rect.top = rect[0],rect[1]
        # 获取太阳花图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置太阳花的生命状态  True活的，false死的
        self.active = True
        # 加载太阳花动作
        self.images = []
        self.images.extend([pygame.image.load("../material/images/SunFlower_00.png")
                                    ,pygame.image.load("../material/images/SunFlower_01.png")
                                    ,pygame.image.load("../material/images/SunFlower_02.png")
                                    ,pygame.image.load("../material/images/SunFlower_03.png")
                               , pygame.image.load("../material/images/SunFlower_04.png")
                               , pygame.image.load("../material/images/SunFlower_05.png")
                               , pygame.image.load("../material/images/SunFlower_06.png")
                               , pygame.image.load("../material/images/SunFlower_07.png")
                               , pygame.image.load("../material/images/SunFlower_08.png")
                               , pygame.image.load("../material/images/SunFlower_09.png")
                               , pygame.image.load("../material/images/SunFlower_10.png")
                               , pygame.image.load("../material/images/SunFlower_11.png")
                               , pygame.image.load("../material/images/SunFlower_12.png")
                            ])

