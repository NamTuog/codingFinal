import pygame, sys, StartScreen, Level1
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
    SCREEN.blit(StartScreen.create_Font("Play Game", 22, StartScreen.showthis.button1colour), (80, 250))
    #Check if the mouse is pressing the button (Currently have a placeholder instead of calling level 1)
    StartScreen.showthis.mousecheck()
    pygame.display.update()

Level1.init_1()
while level1 == True:
    for enemy in enemies:
        SCREEN.blit(enemy.img,enemy.rect)
    for spike in spikes
        SCREEN.blit(SPIKE.png, spike.rect)
    screen.blit(Dave.rect)