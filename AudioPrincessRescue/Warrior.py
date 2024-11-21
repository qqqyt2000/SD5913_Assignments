import pygame

class ControlImage:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_size()
        self.x = 100
        self.y = 100

    def update_position(self):
        # 获取键盘输入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 10
        if keys[pygame.K_RIGHT]:
            self.x += 10
        if keys[pygame.K_UP]:
            self.y -= 10
        if keys[pygame.K_DOWN]:
            self.y += 10

        # 限制键盘控制的物体在屏幕内
        self.x = max(0, min(self.x, 640 - self.width))
        self.y = max(0, min(self.y, 480 - self.height))

    def reset_position(self):
        self.x = 100
        self.y = 100

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))