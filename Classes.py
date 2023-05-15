import pygame, sys


class Dave():
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.size = (12,12)
        self.health = 1
        self.speed = 1
        self.img = pygame.image.load('IDLE1.png')
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
        ground = 0 #TEMPORARY

        self.movement_x = 0
        self.movement_y = 0

        # Left
        if self.left and self.x > -1:  # and not self.right
            self.movement_x = - self.speed

            # Right
        elif self.right and self.x <= 1570:
            self.movement_x = self.speed

            # Down
        elif self.down and self.y >= 0:
            self.movement_y = self.speed * 0.8

        # Jumping
        if self.up and self.rect.colliderect(ground) and not self.jump:
            self.jump = True
            self.movement_y = -self.jump_speed * 2

        # Diagonal Movements

        if self.left and self.up and self.x > -1 and self.y <= 904:
            if self.jump == False:
                self.jump = True
                self.movement_x = -self.speed
                self.movement_y = -self.jump_speed
            else:
                pass


        elif self.left and self.down and self.x > -1 and self.y >= 0:
            self.movement_x = -self.speed
            self.movement_y = self.speed * 0.8


        elif self.right and self.up and self.x <= 1570 and self.y <= 904:
            if self.jump == False:
                self.jump = True
                self.movement_x = self.speed
                self.movement_y = -self.jump_speed
            else:
                pass

        elif self.right and self.down and self.y >= 0 and self.x <= 1570:
            self.movement_x = self.speed
            self.movement_y = self.speed * 0.8
        # Updating to the final location (x and y)
        self.x += self.movement_x
        self.y += self.movement_y

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    def fall(self):
        ground = 0 #TEMPORARY
        if not self.rect.colliderect(ground):  # If the player is not on the ground (on the sky)
            self.movement_y += 2.5  # Falls down to the ground with the speed of 3.
        else:
            self.jump = False

            # Updating to the final location (x and y)
        self.x += self.movement_x
        self.y += self.movement_y

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    def die(self):
            game = 0
            #Restart game

class Robot():
    def __init__(self):
        self.size = #


class Alien():
    def __init__(self):
        self.size = #