import pygame
import random

class Pizza():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images\pizza.png').convert()
		#设置rect属性
        self.rect = self.image.get_rect()
        #
        self.rect.centerx =  random.randint(100,800)
        self.rect.centery =  random.randint(100,500)
    
    def update(self):
        self.rect.centerx =  random.randint(100,800)
        self.rect.centery =  random.randint(100,500)
    
    def blitme(self):
        '''指定位置绘制披萨'''
        self.screen.blit(self.image, self.rect)
