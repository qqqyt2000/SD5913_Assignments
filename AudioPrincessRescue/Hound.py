import pygame
import random

class RandomImage:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_size()
        self.x = random.randint(0, 480 - self.width)
        self.y = random.randint(0, 480 - self.height)
        self.last_change_time = pygame.time.get_ticks()

    def update_position(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time > 1500:
            self.x = random.randint(0, 480 - self.width)
            self.y = random.randint(0, 480 - self.height)
            self.last_change_time = current_time

    def reset_position(self):
        self.x = random.randint(0, 480 - self.width)
        self.y = random.randint(0, 480 - self.height)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))