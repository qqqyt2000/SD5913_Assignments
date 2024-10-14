import pygame

class PG1():
	
	def __init__(self, screen):
        #初始化P1并设置初始位置
		self.screen = screen
		
		self.image = pygame.image.load('images\penguin.png').convert()
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
        #屏幕底端右侧
		self.rect.right = self.screen_rect.right 
		self.rect.bottom = self.screen_rect.bottom
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def update(self):
        #连续移动，不飞出屏幕
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx  += 1
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 1
		if self.moving_up and self.rect.top >0:
			self.rect.centery -= 1
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 1
		
			
	def blitme(self):
        #指定位置绘制角色
		self.screen.blit(self.image, self.rect)

class PG2():
	
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load('images\pg1.png').convert()
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.left = self.screen_rect.left
		self.rect.bottom = self.screen_rect.bottom
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx  += 1
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 1
		if self.moving_up and self.rect.top >0:
			self.rect.centery -= 1
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 1
		
			
	def blitme(self):
		self.screen.blit(self.image, self.rect)

