# usr/bin/python
# Author:yxy
# -*- coding: utf-8 -*-
import pygame
class SurFace(pygame.sprite.Sprite):   #有图片或者动态图片时就需要继承sprite
    def __init__(self,bg_size):
        super(SurFace,self).__init__()

        self.background = "../material/images/Surface.png"
        self.background_image = pygame.image.load(self.background).convert()

        self.image1 = pygame.image.load("../material/images/1.png")
        self.image2 = pygame.image.load("../material/images/2.png")
        self.image3 = pygame.image.load("../material/images/3.png")
        self.image4 = pygame.image.load("../material/images/4.png")
        self.image5 = pygame.image.load("../material/images/5.png")
        self.image6 = pygame.image.load("../material/images/6.png")
        self.image7=pygame.image.load("../material/images/Help.png")
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = 700, 50
        self.mask = pygame.mask.from_surface(self.image1)


