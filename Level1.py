Import pygame
import Spike, Alien, Robot, Dave

def init_1():   # Creates and moves all assests for the first level
    spikes = ()
    enemies = ()
    Dave.rect = Dave.rect.move()
    spike = Spike.Spike()
    spikes.append(spike)
    spike = Spike.Spike()
    spikes.append(spike)
    spike = Spike.Spike()
    spikes.append(spike)
    spike = Spike.Spike()
    spikes.append(spike)
    alien = Alien.Alien()
    enemies.append(alien)