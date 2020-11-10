"""
Object programming
init constructor

Zad rakieta
napisz program ktory sklada sie z 5 rakiet , gdzie losowo podany jest ruch
"""
import random


class Rocket:

    def __init__(self, name, speed):
        self.level_start = 0
        self.speed = speed
        self.name = name

    def fly(self):
        self.level_start += self.speed


rockets = [Rocket("Rocket" + str(i), random.randint(0, 5)) for i in range(5)]


for _ in range(10):
    RocketIndexToMove = random.randint(0, 4)
    rockets[RocketIndexToMove].fly()

for rocket in rockets:
    print(rocket.name, rocket.speed, rocket.level_start)
