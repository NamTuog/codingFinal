import pygame


class Lv1():
    def __init__(self):
        self.image = pygame.image.load("Images/WORLD1BACKGROUND.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def init_1(self,Dave,Spike,Alien):   # Creates and moves all assests for the first level
        spikes = []
        enemies = []
        Dave = Dave.Dave(125,10)
        Dave.rect = Dave.rect.move(125,10)
        spike = Spike.Spike(200, 10)
        spikes.append(spike)
        spike = Spike.Spike(210,10)
        spikes.append(spike)
        spike = Spike.Spike(220,10)
        spikes.append(spike)
        spike = Spike.Spike(230,10)
        spikes.append(spike)
        alien = Alien.Alien(240,10,10)
        enemies.append(alien)
        return spikes, enemies

def update(Lv1,enemies,spikes,Dave):
    SCREEN.blit(Lv1.image, Lv1.rect)
    for enemy in enemies:
        SCREEN.blit(enemy.img,enemy.rect)
    for spike in spikes:
        SCREEN.blit(SPIKE.png, spike.rect)
    SCREEN.blit(Dave.rect)