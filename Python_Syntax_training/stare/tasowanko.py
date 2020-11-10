"""
shuffle - randomize entiire list
"""

import random

cardList = ["9","9","9","9","10","10","10","10",
            "Jack","Jack","Jack","Jack",
            "Queen","Queen","Queen","Queen",
            "King","King","King","King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker","Joker"]
print(cardList)
random.shuffle(cardList)
