"""
metody typu d under - DOUBLE underscore
__str__ - STRing
"""


import random


class Rocket:

    def __init__(self, name, speed=1):
        self.altitude = 0

        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest na wysokosci" + str(self.altitude)


rockets = [Rocket(random.randint(1, 6))
           for _ in range(5)]

for _ in range(10):
    RocketIndexToMove = random.randint(0, 4)
    rockets[RocketIndexToMove].moveUp()

for rocket in rockets:
    print(rocket)
