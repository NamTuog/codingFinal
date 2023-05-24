import pygame, Images

items = []
class SpeedUp: # Item gives player a speed up at tho cost of a jump down
    def __init__(self,x,y): # Creates self and takes spawn point
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('SPEEDBOOSTITEM.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(self.x, self.y)
    def collectSpeed(self):
        self.kill

class JumpUp: # Item gives player a jump up at tho cost of a speed down
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('JUMPBOOSTITEM.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(self.x, self.y)

    def collectJump(self):
            self.kill()

class Sub(): # Grants the player temporary immortality
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('Sub.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(self.x, self.y)

    def collectSub(self):
        self.kill