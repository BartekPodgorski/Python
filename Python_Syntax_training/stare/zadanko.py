"""
napisz funkcje ktora zasymuluuje totka 6 z 49
sample wali unikalnie jezeli sa unikalne wartosci w liscie
set ucina powtorki
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



"""
def choose_numbers(amount,total_amount):
    print(random.sample(range(total_amount+1),amount))

choose_numbers(6,49)
"""
"""
container = []

def choose_lotto(amount,total_amount):
    i = 0
    while i < amount:
        x = random.randint(0,total_amount)
        if(x not in container):
            container.append(x)
        else:
            continue
        i += 1

choose_lotto(6,49)
print(container)
"""
