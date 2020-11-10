"""
import random
#random lliczby generowane od 0 do 1
#uniform liczby generowane od 0 do x (float)
# randrage liczby losowe od x do y integer bez y
# randint liczby losowe od x do y wlacznie z y calkowite



def test(weapon_chance):
    chance_hit = random.uniform(0,100)
    if(chance_hit < weapon_chance):
        return "hit"
    else:
        return "don't hit"
x = 0    
trafienie = []
while x <1000:
    trafienie.append(test(50))
    x += 1

#tworzenie na zliczanie i dunkcja counter
from collections import Counter

dictionaryHit = Counter(trafienie)
"""

"""
choice - zwraca losowy element
choices - zwraca liste elemetow i ma wieksze mozliwosci
"""
