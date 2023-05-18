import pygame
import Items

class Dave():
    def __init__(self, x, y):
        self.size = (100, 100)
        self.x = int(x)
        self.y = int(y)
        self.health = 1
        self.speed = 1
        self.default_img = pygame.image.load('IDLE1.png')
        self.img = self.default_img
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.box = pygame.Rect(self.x, self.rect.y, self.rect.width - 20, self.rect.height)

        # Changing images
        self.image_frame = 1
        self.img_time = 0
        self.img_change = False
        self.image_flipped = False

        # Directions
        self.left = False
        self.right = False
        self.down = False

        # X/Y coordinates
        self.movement_x = 0
        self.movement_y = 0

        # Jump
        self.up = False
        self.jump = False
        self.jump_speed = 20

    def move(self, ground, platform):
        self.movement_x = 0
        self.movement_y = 0

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

            # Down
        elif self.down and self.y >= 0:
            self.movement_y = self.speed

            # Up
        if self.up and not self.jump:
            self.jump = True
            self.movement_y = -self.jump_speed * 2

        # Diagonal (Left + Jump)

        if self.left and self.up and self.x > -1 and self.y <= 320:
            if self.jump == False:
                self.jump = True
                self.movement_x = -self.speed
                self.movement_y = -self.jump_speed
            else:
                pass

        # Diagonal (Right + Up)

        elif self.right and self.up and self.x <= 320 and self.y <= 304:
            if self.jump == False:
                self.jump = True
                self.movement_x = self.speed
                self.movement_y = -self.jump_speed
            else:
                pass

        # Location Updating
        self.x += self.movement_x
        self.y += self.movement_y

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

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    # Gravity
    def fall(self, ground, platform):

        self.box.x = self.x
        self.box.y = self.y

        if not self.box.colliderect(ground):
            if self.box.colliderect(platform):
                if self.up:
                    self.jump = True
                    self.movement_y = -self.jump_speed * 2.5
                else:
                    self.movement_y = 0
            else:
                self.movement_y += 1.5
        else:
            self.jump = False

        self.x += self.movement_x
        self.y += self.movement_y

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    def pickup(self):
        for item in Items.items:
            if pygame.Rect.colliderect(self.rect, Items.SpeedUp.rect):
                speedBoost = True
                Items.SpeedUp.collectSpeed()
                self.health += 1
            if pygame.Rect.colliderect(self.rect, Items.JumpUp.rect):
                jumpBoost = True
                Items.JumpUp.collectJump()
                self.health += 1
            if pygame.Rect.colliderect(self.rect, Items.Subway.rect):
                subBoost = True
                Items.SpeedUp.collectSub()
                self.health += 1
                while self.health > 1:
                    while speedBoost == True:
                        self.speed = self.speed * 1.5
                        self.jump = self.jump * 0.5
                    while jumpBoost == True:
                        self.jump = self.jump * 1.5
                        self.speed = self.speed * 0.5
                    while subBoost = True:
                        for pygame.time.get_ticks() % (20) == 0
                            self.health == 10000
                        self.health = 1
                        subBoost = False
    def die(self):
        game = 0
        # Restart game
