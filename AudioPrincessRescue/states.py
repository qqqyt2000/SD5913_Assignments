import pygame

class States:
    INIT, PLAYING, END = "INIT", "PLAYING", "END"

    def __init__(self):
        self.current_state = self.INIT

    def set_state(self, state):
        self.current_state = state

    def get_state(self):
        return self.current_state

    def handle_init(self, screen, font):
        screen.fill((0, 0, 0))
        play_text = font.render("Play", True, (255, 255, 255))
        screen.blit(play_text, (270, 200))
        pygame.display.flip()

    def handle_end(self, screen, font):
        screen.fill((0, 0, 0))
        end_text = font.render("End", True, (255, 255, 255))
        screen.blit(end_text, (270, 200))
        pygame.display.flip()
