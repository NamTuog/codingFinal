Import pygame
import Spike, Alien, Robot, Dave

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

def