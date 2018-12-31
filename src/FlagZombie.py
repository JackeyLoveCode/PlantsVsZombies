'''旗帜僵尸'''
import pygame


class FlagZombie(pygame.sprite.Sprite):
    energy = 40
    def __init__(self,bg_size):
        super(FlagZombie, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #图片
        self.image = pygame.image.load("../material/images/FlagZombie_0.png")
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
        #设置僵尸的生命
        self.energy = FlagZombie.energy
        # 加载僵尸动作
        self.images = []
        self.images.extend([pygame.image.load("../material/images/FlagZombie_0.png")
                                    ,pygame.image.load("../material/images/FlagZombie_1.png")
                                    ,pygame.image.load("../material/images/FlagZombie_2.png")
                                    ,pygame.image.load("../material/images/FlagZombie_3.png")
                               , pygame.image.load("../material/images/FlagZombie_4.png")
                               , pygame.image.load("../material/images/FlagZombie_5.png")
                               , pygame.image.load("../material/images/FlagZombie_6.png")
                               , pygame.image.load("../material/images/FlagZombie_7.png")
                               , pygame.image.load("../material/images/FlagZombie_8.png")
                               , pygame.image.load("../material/images/FlagZombie_9.png")
                               , pygame.image.load("../material/images/FlagZombie_10.png")
                               , pygame.image.load("../material/images/FlagZombie_11.png")

                            ])
        self.dying_images = []
        self.dying_images.extend([pygame.image.load("../material/images/ZombieDie_0.png")
                               , pygame.image.load("../material/images/ZombieDie_1.png")
                               , pygame.image.load("../material/images/ZombieDie_2.png")
                               , pygame.image.load("../material/images/ZombieDie_3.png")
                               , pygame.image.load("../material/images/ZombieDie_4.png")
                               , pygame.image.load("../material/images/ZombieDie_5.png")
                               , pygame.image.load("../material/images/ZombieDie_6.png")
                               , pygame.image.load("../material/images/ZombieDie_7.png")
                               , pygame.image.load("../material/images/ZombieDie_8.png")
                               , pygame.image.load("../material/images/ZombieDie_9.png")

                            ])
    def move(self):
        if self.rect.left > 250:
            self.rect.left -= self.speed
