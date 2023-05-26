#import pygame
import Classes.Spike, Classes.Alien, Classes.Robot, Classes.Dave

def init_1():   # Creates and moves all assests for the first level
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

W1.image = pygame.image.load("Images/WORLD1BACKGROUND.png")
W1.image = pygame.transform.scale(W1.image, (800, 600))
W1.rect = W1.image.get_rect()
def update():
    SCREEN.blit(W1.image, W1.rect)
    for enemy in enemies:
        SCREEN.blit(enemy.img,enemy.rect)
    for spike in spikes:
        SCREEN.blit(SPIKE.png, spike.rect)
    SCREEN.blit(Dave.rect)