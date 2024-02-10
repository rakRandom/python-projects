import pygame


class Debug:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 14)

    def show(self, message):
        text = self.font.render(message, False, 'yellow', 'black')
        self.screen.blit(text, (0, 0))
