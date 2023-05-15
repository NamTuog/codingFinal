


class Dave():
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.size = (12,12)
        self.health = 1
        self.speed = 1
        self.img = pygame.iamge.load('IDLE1.png')
        self.img = pygame.transform.scale(self.img,self.size)
        self.rect = self.img.get_rect()
        # Directions (only = True when the key is pressed)
        self.left = False
        self.right = False
        self.down = False
        # Movement of the player. Is added to the X/Y coordinates after clicking.
        self.movement_x = 0
        self.movement_y = 0
        # Jumping
        self.up = False
        self.jump = False
        self.jump_speed = 25

    def move(self):    #including jump


    def fall(self):



class Robot():


class Alien():