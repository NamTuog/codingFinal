import pygame, sys, StartScreen
from pygame.locals import QUIT


pygame.init()
SCREEN = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Displays the background photo for the Menu
    SCREEN.blit(StartScreen.showthis.image, StartScreen.showthis.rect)
    #Displays the first button for the menu
    StartScreen.showthis.button1(SCREEN)
    pygame.display.update()
