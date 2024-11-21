import pygame

import pygame

class Button:
    def __init__(self, image_path, position, image_scale=(1, 1), bg_color=(135, 135, 135)):
        self.image_path = image_path
        self.position = position
        self.image_scale = image_scale
        self.bg_color = bg_color
        self.image = None
        self.rect = None
        self.update()

    def update(self):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.image_scale[0]), int(self.image.get_height() * self.image_scale[1])))
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)