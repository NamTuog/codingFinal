
class Alien():
    def __init__(self,lx,rx,wany):
        self.size = (20,20)
        self.speed = 5
        self.img = pygame.image.load('WALK2.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()


    def wander(self):