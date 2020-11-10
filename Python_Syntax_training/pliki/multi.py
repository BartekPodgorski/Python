"""
podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:
r+ - do czytania i pisania

file.read file.write

w+ - do pisania i czytania
różni sie tym, że usunie zawartość istniejącego pliku
lub stworzy plik gdy go nie było

a+ - "wieczny tryb" dopisywania i przy okazji czytania
UWAGA! wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istniał - stworzy go

"""

with open("oceany.txt","r",encoding = "UTF-8") as file:
    oceany = file.read("\n")
