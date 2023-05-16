import pygame


#The menu class
class menu:
    def __init__(self):
        self.image = pygame.image.load("Images/TITLE.png")
        self.rect = self.image.get_rect()
        #Defines the first button for the menu
    def button1(self,screen):
        self.button1set = pygame.draw.rect(screen, (255, 0, 0), (30, 30, 30, 30))
        return self.button1set


showthis = menu()

