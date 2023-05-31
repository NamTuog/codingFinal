import pygame, sys, StartScreen, Level1, time
from Classes import Dave, Spike, Alien, Items
from pygame.locals import QUIT


pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dave's Dash")
clock = pygame.time.Clock()



# MAIN MENU
Level = 0
while Level != 1:
    clock.tick(30)
    # Mouse tracking function that I sorta kinda took (WIP)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            print("x = {}, y = {}".format(pos[0], pos[1]))  #TEMPORARY
    #Displays the background photo for the Menu
    SCREEN.blit(StartScreen.showthis.image, StartScreen.showthis.rect)
    #Displays the title
    SCREEN.blit(StartScreen.create_Font("DAVE'S DASH", 88), (30, 10))
    #Displays the first button for the menu
    StartScreen.showthis.button1(SCREEN)
    SCREEN.blit(StartScreen.create_Font("Play Game", 22, StartScreen.showthis.button1colour), (80, 250))
    #Check if the mouse is pressing the button (Currently have a placeholder instead of calling level 1)
    Level = StartScreen.showthis.mousecheck()
    pygame.display.update()


#LEVEL 1 START
Lv1 = Level1.Lv1()
spikes, enemies, Dave = Level1.Lv1.init_1(Lv1,Dave,Spike,Alien)
while Level == 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Level1.update(Lv1,enemies,spikes,Dave,SCREEN,Alien)
    pygame.display.update()