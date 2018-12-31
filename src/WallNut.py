'''坚果'''
import pygame


class WallNut(pygame.sprite.Sprite):
    def __init__(self,rect,bg_size):
        super(WallNut, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #图片
        self.image = pygame.image.load("../material/images/WallNut_00.png")
        # 获取图片位置
        self.rect = self.image.get_rect()
        # 定义坚果的初始化位置
        self.rect.left, self.rect.top = rect[0],rect[1]
        # 获取坚果图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置太阳的生命状态  True存活，false死亡
        self.active = True
        # 加载坚果动作
        self.images = []
        self.images.extend([pygame.image.load("../material/images/WallNut_00.png")
                                    ,pygame.image.load("../material/images/WallNut_01.png")
                                    ,pygame.image.load("../material/images/WallNut_02.png")
                                    ,pygame.image.load("../material/images/WallNut_03.png")
                               , pygame.image.load("../material/images/WallNut_04.png")
                               , pygame.image.load("../material/images/WallNut_05.png")
                               , pygame.image.load("../material/images/WallNut_06.png")
                               , pygame.image.load("../material/images/WallNut_07.png")
                               , pygame.image.load("../material/images/WallNut_08.png")
                               , pygame.image.load("../material/images/WallNut_09.png")
                               , pygame.image.load("../material/images/WallNut_10.png")
                               , pygame.image.load("../material/images/WallNut_11.png")
                               , pygame.image.load("../material/images/WallNut_12.png")

                            ])

