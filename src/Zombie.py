'''僵尸'''
import pygame
from random import randint

class Zombie(pygame.sprite.Sprite):
    energy = 20
    def __init__(self,bg_size):
        super(Zombie, self).__init__()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        #图片
        self.image = pygame.image.load("../material/images/Zombie_0.png")
        # 获取图片位置
        self.rect = self.image.get_rect()
        # 定义僵尸的初始化位置
        self.rect.left, self.rect.top = randint(900,1200),randint(0,400)
        # 获取僵尸图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置僵尸的生命状态  True活的，false死的
        self.active = True
        #僵尸是否遇到坚果
        self.isMeetWallNut = False
        #僵尸是否遇到豌豆射手
        self.isMeetPeashooter = False
        #僵尸是否遇到太阳花
        self.isMeetSunFlower = False
        #设置僵尸移动速度
        self.speed = 2
        #设置僵尸的生命
        self.energy = Zombie.energy
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

        self.attack_images = []
        self.attack_images.extend([pygame.image.load("../material/images/ZombieAttack_0.png")
                               , pygame.image.load("../material/images/ZombieAttack_1.png")
                               , pygame.image.load("../material/images/ZombieAttack_2.png")
                               , pygame.image.load("../material/images/ZombieAttack_3.png")
                               , pygame.image.load("../material/images/ZombieAttack_4.png")
                               , pygame.image.load("../material/images/ZombieAttack_5.png")
                               , pygame.image.load("../material/images/ZombieAttack_6.png")
                               , pygame.image.load("../material/images/ZombieAttack_7.png")
                               , pygame.image.load("../material/images/ZombieAttack_8.png")
                               , pygame.image.load("../material/images/ZombieAttack_9.png")
                               , pygame.image.load("../material/images/ZombieAttack_10.png")
                               , pygame.image.load("../material/images/ZombieAttack_11.png")
                               , pygame.image.load("../material/images/ZombieAttack_12.png")
                               , pygame.image.load("../material/images/ZombieAttack_13.png")
                               , pygame.image.load("../material/images/ZombieAttack_14.png")
                               , pygame.image.load("../material/images/ZombieAttack_15.png")
                               , pygame.image.load("../material/images/ZombieAttack_16.png")
                               , pygame.image.load("../material/images/ZombieAttack_17.png")
                               , pygame.image.load("../material/images/ZombieAttack_18.png")
                               , pygame.image.load("../material/images/ZombieAttack_19.png")
                               , pygame.image.load("../material/images/ZombieAttack_20.png")])
    def move(self):
        if not self.isMeetWallNut:
            if self.rect.left > 150:
                self.rect.left -= self.speed

