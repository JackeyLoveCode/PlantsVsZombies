'''太阳'''
import pygame


class Sun(pygame.sprite.Sprite):
    sunFlower_left = sunFlower_top = 0
    def __init__(self,rect,bg_size):
        super(Sun, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #太阳花的位置
        self.sunFlower_left,self.sunFlower_top = rect.left,rect.top
        #图片
        self.image = pygame.image.load("../material/images/Sun_1.png")
        # 获取图片位置
        self.rect = self.image.get_rect()
        # 定义太阳的初始化位置
        self.rect.left, self.rect.top = self.sunFlower_left + 20,self.sunFlower_top + 20
        # 获取太阳图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置太阳的生命状态  True没有被收集，false已经被收集
        self.active = True
        # 加载太阳动作
        self.images = []
        self.images.extend([pygame.image.load("../material/images/Sun_1.png")
                                    ,pygame.image.load("../material/images/Sun_2.png")
                                    ,pygame.image.load("../material/images/Sun_3.png")
                                    ,pygame.image.load("../material/images/Sun_4.png")
                               , pygame.image.load("../material/images/Sun_5.png")
                               , pygame.image.load("../material/images/Sun_6.png")
                               , pygame.image.load("../material/images/Sun_7.png")
                               , pygame.image.load("../material/images/Sun_8.png")
                               , pygame.image.load("../material/images/Sun_9.png")
                               , pygame.image.load("../material/images/Sun_10.png")
                               , pygame.image.load("../material/images/Sun_11.png")
                               , pygame.image.load("../material/images/Sun_12.png")
                               , pygame.image.load("../material/images/Sun_13.png")
                               , pygame.image.load("../material/images/Sun_14.png")
                               , pygame.image.load("../material/images/Sun_15.png")
                               , pygame.image.load("../material/images/Sun_16.png")
                               , pygame.image.load("../material/images/Sun_17.png")
                            ])

