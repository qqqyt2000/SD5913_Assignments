import pygame

class CollisionDetector:
    def __init__(self, control_image, audio_image, random_image):
        self.control_image = control_image
        self.audio_image = audio_image
        self.random_image = random_image

    def detect_collision(self):
        control_rect = pygame.Rect(self.control_image.x, self.control_image.y, self.control_image.width, self.control_image.height)
        audio_rect = pygame.Rect(self.audio_image.x, self.audio_image.y, self.audio_image.width, self.audio_image.height)
        random_rect = pygame.Rect(self.random_image.x, self.random_image.y, self.random_image.width, self.random_image.height)

        if control_rect.colliderect(audio_rect) or control_rect.colliderect(random_rect):
            return True
        else:
            return False

    def detect_game_over(self, elapsed_time):
        if self.control_image.x > 500:
            return "Warrior Win!"
        elif elapsed_time > 120:
            return "Guards Win!"
        else:
            return None