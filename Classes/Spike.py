import pygame


class Spike():
    def __init__(self): # Get x,y for location of spike
        self.img = pygame.image.load('Images/SPIKE.png')
        self.rect = self.img.get_rect()
        #self.rect.move(x, y)

    # Add spikes to list when initialized, for easier collision check