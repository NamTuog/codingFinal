import pygame

class Spike():
    def __init__(self,x,y): # Get x,y for location of spike
        self.x = x
        self.y = y
        self.img = pygame.load.image('SPIKE.ing')
        self.rect = pygame.get_rect(self.img)
        self.rect.move(x,y)

    # Add spikes to list when initialized, for easier collision check