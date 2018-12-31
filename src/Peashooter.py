'''豌豆射手'''
import pygame


class Peashooter(pygame.sprite.Sprite):
    def __init__(self,rect,bg_size):
        super(Peashooter, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #图片
        self.image = pygame.image.load("../material/images/Peashooter_00.png")
        # 获取图片位置
        self.rect = self.image.get_rect()
        # 定义豌豆的初始化位置
        self.rect.left, self.rect.top = rect[0],rect[1]
        # 获取豌豆图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置豌豆的生命状态  True活的，false死的
        self.active = True
        # 加载豌豆动作
        self.images = []
        self.images.extend([pygame.image.load("../material/images/Peashooter_00.png")
                                    ,pygame.image.load("../material/images/Peashooter_01.png")
                                    ,pygame.image.load("../material/images/Peashooter_02.png")
                                    ,pygame.image.load("../material/images/Peashooter_03.png")
                               , pygame.image.load("../material/images/Peashooter_04.png")
                               , pygame.image.load("../material/images/Peashooter_05.png")
                               , pygame.image.load("../material/images/Peashooter_06.png")
                               , pygame.image.load("../material/images/Peashooter_07.png")
                               , pygame.image.load("../material/images/Peashooter_08.png")
                               , pygame.image.load("../material/images/Peashooter_09.png")
                               , pygame.image.load("../material/images/Peashooter_10.png")
                               , pygame.image.load("../material/images/Peashooter_11.png")
                               , pygame.image.load("../material/images/Peashooter_12.png")
                            ])

