import random
from math import sqrt


class Rocket:

    id = 0

    def __init__(self, speed: float = 1, altitude: float = 0, x: float = 0):
        self.altitude = altitude

        self.speed = speed

        self.x = x

        Rocket.id += 1
        self.id = Rocket.id

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest na wysokosci: " + str(self.id) + " "+ str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(random.randint(1, 6))
                        for _ in range(amountOfRockets)]

        for _ in range(10):
            RocketIndexToMove = random.randint(0, len(self.rockets) - 1)
            self.rockets[RocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1: Rocket, rocket2: Rocket) -> float:
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)

    def __len__(self):
        return len(self.rockets)
