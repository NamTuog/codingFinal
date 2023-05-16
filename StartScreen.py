import pygame




class menu:
    def __init__(self):
        self.image = pygame.image.load("Images/TITLE.png")
        self.rect = self.image.get_rect()


display = menu()

