"""
PLIK - nazwana lokacja, która przechowuje na STAŁE dane na dysku.

RAM - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO

Operacje na plikach
1) otwieranie
2) pisanie/czytanie
3) zamykanie

podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy
             rozpoznawały plik w odpowiedni dla tych programów sposób
"""
"""
read - r czyta pliki , podajemy jeszcze sposob kodowania
readline - pokazuje tylko pierwszy wers
readlines - pokazuje wszsytkie wersy
tell - mowi , gdzie skonczylismy ostatnia operacje na pliku
seek - szuka(zmienia) - na miejsce wskazane przez nas
"""
"""
with open("oceany.txt", "r", encoding = "UTF-8") as file:
   for line in file:
       print(line)
"""
'''
with open("oceany.txt", "r", encoding = "UTF-8") as file:
    print(file.read())
    file.seek(0)
    print(file.read())
'''
with open("oceany.txt","a",encoding = "UTF-8") as file:
    file.write("\nPółnocny")
    
