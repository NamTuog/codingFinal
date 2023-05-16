import pygame

class SpeedUp():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('SpeedUp.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(x, y)

    def collectSpeed(self,Dave.rect):
        if pygame.Rect.colliderect(Dave.rect,self.rect):
            self.rect.move(-20,-20)

class JumpUp():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('JumpUp.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(x, y)

    def collectJump(self,Dave.rect):
        if pygame.Rect.colliderect(Dave.rect,self.rect):
            self.rect.move(-20,-20)

class Sub():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = (5,5)
        self.img = pygame.image.load('Sub.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.rect.move(x,y)

    def collectSub(self,Dave.rect):
        if pygame.Rect.colliderect(Dave.rect,self.rect):
            self.rect.move(-20,-20)