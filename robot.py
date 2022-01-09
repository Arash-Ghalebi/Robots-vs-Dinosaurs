from weapon import Weapon
from random import *

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Positron Cannon', 20, 0)

    def attack(self, dinosaur):
        dino_opponent = dinosaur
        if self.weapon.crit_chance >= randint(1, 100):
            dino_opponent.health = dino_opponent.health - (self.weapon.attack_power * 3)
            print("Critical Strike!\n")
        else:    
            dino_opponent.health = dino_opponent.health - self.weapon.attack_power
        return dino_opponent.health