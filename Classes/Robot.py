
class Robot():
    def __init__(self):
        self.size = (30,30)
        self.speed = 2
        self.img = pygame.image.load('ROBOT.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
    def wander(self):