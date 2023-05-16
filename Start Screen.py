import pygame, sys

from main import DISPLAYSURF


class menu:
  def __init__(self):
    self.image=pygame.image.load("Images/TITLE.png")
    self.rect = self.image.get_rect()

#Starts the menu screen
display=menu()
DISPLAYSURF.blit(display.image, display.rect)
pygame.draw.rect(DISPLAYSURF, (255, 0, 0), pygame.Rect(100, 30, 60, 60))