'''僵尸'''
import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        super(Zombie, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #图片
        self.image = pygame.image.load("../material/images/Zombie_0.png")
        # 获取图片位置
        self.rect = self.image.get_rect()
        # 定义僵尸的初始化位置
        self.rect.left, self.rect.top = 1000,50
        # 获取僵尸图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置僵尸的生命状态  True活的，false死的
        self.active = True
        #设置僵尸移动速度
        self.speed = 1
        # 加载僵尸动作
        self.images = []
        self.images.extend([pygame.image.load("../material/images/Zombie_0.png")
                                    ,pygame.image.load("../material/images/Zombie_1.png")
                                    ,pygame.image.load("../material/images/Zombie_2.png")
                                    ,pygame.image.load("../material/images/Zombie_3.png")
                               , pygame.image.load("../material/images/Zombie_4.png")
                               , pygame.image.load("../material/images/Zombie_5.png")
                               , pygame.image.load("../material/images/Zombie_6.png")
                               , pygame.image.load("../material/images/Zombie_7.png")
                               , pygame.image.load("../material/images/Zombie_8.png")
                               , pygame.image.load("../material/images/Zombie_9.png")
                               , pygame.image.load("../material/images/Zombie_10.png")
                               , pygame.image.load("../material/images/Zombie_11.png")
                               , pygame.image.load("../material/images/Zombie_12.png")
                               , pygame.image.load("../material/images/Zombie_13.png")
                               , pygame.image.load("../material/images/Zombie_14.png")
                               , pygame.image.load("../material/images/Zombie_15.png")
                               , pygame.image.load("../material/images/Zombie_16.png")
                               , pygame.image.load("../material/images/Zombie_17.png")
                               , pygame.image.load("../material/images/Zombie_18.png")
                               , pygame.image.load("../material/images/Zombie_19.png")
                               , pygame.image.load("../material/images/Zombie_20.png")
                               , pygame.image.load("../material/images/Zombie_21.png")
                            ])

    def move(self):
        if self.rect.left > 250:
            self.rect.left -= self.speed

