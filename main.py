import pygame, sys
from pygame.locals import QUIT

#The menu
class menu:
  def __init__(self):
    self.image=pygame.image.load("Images/TITLE.png")
    self.rect = self.image.get_rect()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    #Starts the menu screen
    display=menu()
    DISPLAYSURF.blit(display.image, display.rect)
