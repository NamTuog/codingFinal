
class Alien():
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self,lx,rx,wany):
=======
    def __init__(self):
>>>>>>> 3741446 (Work on items)
=======
    def __init__(self):
>>>>>>> origin/main
        self.size = (20,20)
        self.speed = 5
        self.img = pygame.image.load('WALK2.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 3741446 (Work on items)
=======
>>>>>>> origin/main
    def wander(self):