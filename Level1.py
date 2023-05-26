import pygame
import Dave, Spike, Alien

class Lv1():
    def __init__(self):
        self.image = pygame.image.load("Images/WORLD1BACKGROUND.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def init_1(self):   # Creates and moves all assests for the first level
        spikes = ()
        enemies = ()
        Dave.rect = Dave.rect.move(125,10)
        spike = Spike.Spike(200, 10)
        spikes.append(spike)
        spike = Spike.Spike(210,10)
        spikes.append(spike)
        spike = Spike.Spike(220,10)
        spikes.append(spike)
        spike = Spike.Spike(230,10)
        spikes.append(spike)
        alien = Alien.Alien(240,10)
        enemies.append(alien)

    def update(self,enemies,spikes):
        SCREEN.blit(self.image, self.rect)
        for enemy in enemies:
            SCREEN.blit(enemy.img,enemy.rect)
        for spike in spikes:
            SCREEN.blit(SPIKE.png, spike.rect)
        SCREEN.blit(Dave.rect)