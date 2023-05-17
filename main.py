import pygame, sys, StartScreen
from pygame.locals import QUIT


pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Mouse tracking function that I sorta kinda took (WIP)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            print("x = {}, y = {}".format(pos[0], pos[1]))
    #Displays the background photo for the Menu
    SCREEN.blit(StartScreen.showthis.image, StartScreen.showthis.rect)
    #Displays the title
    SCREEN.blit(StartScreen.create_Font("DAVE'S DASH", 88), (30, 10))
    #Displays the first button for the menu
    StartScreen.showthis.button1(SCREEN)
    SCREEN.blit(StartScreen.create_Font("Play Game"), (80, 250))
    pygame.display.update()
