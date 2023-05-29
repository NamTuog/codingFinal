import pygame, time

class Dave():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = (100, 100)
        self.health = 1
        self.speed = 4
        self.default_img = pygame.image.load('Images/IDLE1.png')  # First image
        self.image = self.default_img
        self.rect = self.image.get_rect()

        # movements (jump)
        self.jump = False  # Check if Jumping is true or not
        self.jump_time = 0  # Duration of Jumping
        self.velocity_y = 0  # Speed of Jumping and Gravity

        # Changing Images
        self.image_frame = 1  # Frame for change
        self.image_time = 0  # Duration
        self.image_Change = False  # Walking motion
        self.image_Flipped = False

        self.rect.x = self.x
        self.rect.y = self.y

    def move(self, platform, ground):
        # Movements
        self.movement_x = 0  # X movements that are totally added
        self.movement_y = 0  # Y movements that are totallya dded

        # Key
        key = pygame.key.get_pressed()

        # Left & Right Keys
        if key[pygame.K_LEFT]:
            self.movement_x = - self.speed  # Backwards
            self.image_Change = True
            self.image_Flipped = True  # Flip image to the left

        if key[pygame.K_RIGHT]:
            self.movement_x = self.speed  # Right side
            self.image_Change = True
            self.image_Flipped = False  # Not flipping the iamge

        # Jumping

        if not self.jump:  # Prevents Double Jumps
            if key[pygame.K_UP] or key[pygame.K_SPACE]:  # When the Up or space is pressed
                if self.rect.colliderect(ground):  # When colliding with the ground
                    self.jump = True  # Jumping is valid
                    self.jump_time = pygame.time.get_ticks()  # Measure the time
                    self.velocity_y = -10  # Goes Up for 10

        if self.jump:  # While it is jumping
            time_now = pygame.time.get_ticks()  # Time Now
            time_difference = time_now - self.jump_time  # Differnce betwen the time
            if time_difference > 5000:  # If the time difference is bigger than 5000
                self.jump = False  # Jump finishes   (Does not go forever)

        # Walking Motion
        if self.image_Change:  # When self.image_Change is true from left & right movements
            if self.image_frame % 30 == 0:  # Every 10 Frames
                self.image = pygame.image.load('Images/IDLE2.png')  # Load another image
                self.image = pygame.transform.scale(self.image, self.size)
            else:
                self.image = self.default_img  # Go back to the original image
                self.image_Change = False
            self.image_frame += 1

            # Image Switching
        if self.image_Flipped:  # When flipped is true
            self.image = pygame.transform.flip(self.default_img, True, False)  # flip the image

        # Gravity when collding with the platform or the ground
        if not self.rect.colliderect(ground):  # When the player is not colliding with the ground
            if self.rect.colliderect(platform):  # When colliding with the platform
                if self.rect.top > platform.rect.top:  # if platform's top is higher than the self's top
                    self.velocity_y += 1  # Go down (Gravity is Valid)
                elif self.rect.bottom > platform.rect.top:  # If the platform's top is higher than self's bottom
                    self.rect.bottom = platform.rect.top  # The player is over the platform
                    self.velocity_y = 0  # y movement is zero (staying on the platform)
                    if key[pygame.K_UP] or key[pygame.K_SPACE]:  # Jumping is valid on the platform
                        self.jump = True
                        self.velocity_y = -10

            else:  # If the player is not colliding with the platform
                self.velocity_y += 1  # Gravity is valid

        else:
            self.jump = False  # Prevents double jump

        self.movement_y += self.velocity_y  # Add all the velocities including Jump and Gravity to the movement_y
        self.rect.x += self.movement_x  # Move the player
        self.rect.y += self.movement_y  # Move the player

        # Preventing the player to go outside of the screen
        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.movement_y = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.movement_y = 0
        if self.rect.right > 800:
            self.rect.right = 800
            self.movement_x = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.movement_x = 0

    def pickup(self):
        for item in Items.items: # Checks all items in list
            if pygame.Rect.colliderect(self.rect, Items.SpeedUp.rect): # Check for collision "type"
                speedBoost = True   # Effect  = True
                Items.SpeedUp.collectSpeed()    # Remove the item from the screen
                self.health += 1
            if pygame.Rect.colliderect(self.rect, Items.JumpUp.rect):
                jumpBoost = True
                Items.JumpUp.collectJump()
                self.health += 1
            if pygame.Rect.colliderect(self.rect, Items.Subway.rect):
                subBoost = True
                Items.SpeedUp.collectSub()
                self.health += 1
                while self.health > 1:  # While player doesn't take damage
                    while speedBoost == True:   # Grant speed up, jump down
                        self.speed = self.speed * 1.5
                        self.jump = self.jump * 0.5
                    while jumpBoost == True:    # Grants jump up, speed down
                        self.jump = self.jump * 1.5
                        self.speed = self.speed * 0.5
                    while subBoost == True:
                        if self.image_frame % 30 == 0:     # Grants effect for time duration
                            self.health = 9999
                        self.health = 1
                        subBoost = False

    def checkHit(self):     # Check for any collision between the player and any enemy
        if self.health == 0:
            die()
        for spike in spikes():
            if pygame.Rect.colliderect(self.rect, Spike.spike.rect):
                self.health -= 1
        for alien in enemies():
            if pygame.Rect.colliderect(self.rect, Alien.alien.rect):
                self.health -= 1
        for robot in enemies():
            if pygame.Rect.colliderect(self.rect, Robot.robot.rect):
                self.health -= 1

    def die(self):
        game = 0
        # Restart game
