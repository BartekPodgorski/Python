"""
choice - zwraca losowy element
choices - zwraca liste elementow i ma wieksze mozliwosci jak ustalam
to moze byc przyps i p>100
"""

from random import choice,choices

movie_list = ["Tytul 1","Tytul 2","Tytul 3","Tytul 4"]

event = ["smierc", "wygrana", "przegrana","utrata zlota","utrata zycia"]
nagroda_ze_skrzynki = ["zielona","pomaranczowa","purpurowa","legendarne"]
print(choice(movie_list))

from collections import Counter
print(Counter(choices(nagroda_ze_skrzynki,[80,15,4,1],k=10000)))
