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
    SCREEN.blit(StartScreen.display.image, StartScreen.display.rect)
    pygame.display.update()
