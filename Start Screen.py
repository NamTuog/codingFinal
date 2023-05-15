import pygame, sys

class menu:
  def __init__(self):
    self.image=pygame.image.load("Menu.png")
    self.rect = self.image.get_rect()