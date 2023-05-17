import pygame, sys
import Items


class Robot():
    def __init__(self):
        self.size = (30,30)
        self.speed = 2
        self.img = pygame.image.load('ROBOT.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
    def wander(self):


class Alien():
    def __init__(self):
        self.size = (20,20)
        self.speed = 5
        self.img = pygame.image.load('WALK2.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()

    def wander(self):