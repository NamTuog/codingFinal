import pygame

class Lv2():
    def __init__(self):
        self.image = pygame.image.load("Images/WORLD2BACKGROUND.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def init_2(self,Dave,Spike,Alien,FAlien):   # Creates and moves all assests for the first level
        spikes = []
        enemies = []
        Dave.rect = Dave.rect.move(225,550)
        spike = Spike.Spike(200, 10)
        spikes.append(spike)
        spike = Spike.Spike(210,10)
        spikes.append(spike)
        spike = Spike.Spike(620,10)
        spikes.append(spike)
        spike = Spike.Spike(430,10)
        spikes.append(spike)
        alien = Alien.Alien(240,10,10)
        enemies.append(alien)

        return spikes, enemies, Dave

def update(Lv2,enemies,spikes,Dave,SCREEN,Alien):
    SCREEN.blit(Lv2.image, Lv2.rect)
    for alien in enemies:
        SCREEN.blit(alien.img, alien.rect)
    for spike in spikes:
        SCREEN.blit(spike.img, spike.rect)
    SCREEN.blit(Dave.image,Dave.rect)
