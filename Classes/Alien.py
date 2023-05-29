import pygame

class Alien():
    def __init__(self,lx,rx,wany):
        self.size = (20,20)
        self.speed = 5
        self.img = pygame.image.load('Images/WALK2.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()

        # Changing images
        self.image_frame = 1
        self.img_time = 0
        self.img_change = False
        self.image_flipped = False
        # Directions
        self.left = False
        self.right = False



    def wander(self):
        # Left
        if self.left and self.x > -1:  # and not self.right
            self.movement_x = - self.speed
            self.img_change = True
            self.image_flipped = True
            self.img = pygame.transform.flip(self.default_img, True, False)

        # Right
        elif self.right and self.x <= 320:
            self.movement_x = self.speed
            self.img_change = True
            self.image_flipped = False

        # Image Changing / Walking
        if self.img_change == True:
            if self.image_frame % 10 == 0:  # Every 10 frames
                if self.img == self.default_img:
                    self.size = (100, 100)
                    self.img = pygame.image.load('IDLE2.png')
                    self.img = pygame.transform.scale(self.img, self.size)
                else:
                    if self.image_flipped:
                        self.img = pygame.transform.flip(self.default_img, True, False)
                    else:
                        self.img = self.default_img
                        self.img_change = False
            self.image_frame += 1
