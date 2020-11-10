
slownik = {}
x = True

while (x == True):
    wybor = int(input("1 - dodaj definicje, 2 - szukaj definicji, 3 - usun definicje, 4 - wyswietl caly slownik, 5 - zakoncz program: "))
    if (wybor == 1):
        slowo = input("Podaj slowo do dodania: ")
        definicja = input("Podaj definicje do slowa: ")
        slownik.update({slowo:definicja})
        
    elif (wybor == 2):
        szukane = input("Podaj slowo do poszukania: ")
        if(szukane in slownik):
            print(szukane, ":", slownik[szukane])
        else:
            print("Slowa nie ma w slowniku")
            
    elif (wybor == 3):
        usun = input("Podaj slowo do usuniecia: ")
        if(usun == slowo):
            del(slownik[usun])
            print("Slowo", usun, "zostalo usuniete")
        else:
            print("Twoje slowo nie jest w bazie")
        
    elif (wybor == 4):
        print("Oto Twoj slownik:")
        for  key in slownik:
            print("Slowo:", key, "Definicja:", slownik[key])
    elif (wybor == 5):
        x = False
    else:
        print("Nie wybralec zadnej opcji")

 """
problem z tym , ze jak usuwam slowo z bazy to i tak moge je wyswietlic 
    


