import pygame

items = []
class SpeedUp():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('SpeedUp.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(x, y)
    def collectSpeed(self):
            self.kill

class JumpUp():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('JumpUp.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(x, y)

    def collectJump(self):
            self.kill()

class Sub():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('Sub.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(x,y)

    def collectSub(self):
        self.kill