import pygame

from main import DISPLAYSURF


class menu:
    def __init__(self):
        self.image = pygame.image.load("Images/TITLE.png")
        self.rect = self.image.get_rect()


def menuRun():
    display = menu()
    DISPLAYSURF.blit(display.image, display.rect)
