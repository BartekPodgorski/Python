"""
docstring - DOCument String
"""

import random


class Rocket:
    """Cokolwiek tu napisze wypisze sie w rocket = rocket
    """

    def __init__(self, name, speed=1):
        self.altitude = 0

        self.speed = speed

    def moveUp(self):
        """poruszamy sie do gory z  predkoscia speed
        """
        self.altitude += self.speed


rockets = [Rocket(random.randint(1, 6))
           for _ in range(5)]

for _ in range(10):
    RocketIndexToMove = random.randint(0, 4)
    rockets[RocketIndexToMove].moveUp()

for rocket in rockets:
    print(rocket.altitude)
