'''def powitanie (imie):
    print("Czesc",imie,"milo mi Cie przywitac w moim programie")


imiona = ["Arku","Bartku","Karolu"]

for imie in imiona:
    powitanie(imie)


# pole_prostokata

def pole_prostokata(a,b):
    print(a*b)

pole_prostokata(3,5)



def pole_prostokata(a,b):
    return(a*b)

print(5*pole_prostokata(3,5))

def dzielenie(a,b):
    if (b==0):
        return
    else:
    return (a/b)
'''
x=True

def pole_prostokata(a,b):
    return(a*b)

def pole_kwadratu(a):
    return(a*a)

def pole_trojkata(a,h):
    return(a*h/2)

def pole_trapezu(a,b,h):
    return ((a+b)*h/2)

def pole_kola(r):
    return (3.14*r**2)

while (x==True):
    wybor=int(input("Wybierz opcje. 1 - pole prostokata, 2 - pole kwadratu, 3 - pole trojkata, 4  - pole trapezu, 5 - pole kola, 6 - zakoncz program: "))
    if(wybor == 1):
        bok_a = int(input("Podaj dlugosc pierwszego boku: "))
        bok_b = int(input("Podaj dlugosc drugiego boku: "))
        if(bok_a <= 0) | (bok_b <= 0 ):
            print("zle dlugosci bokow")
            continue
        print(pole_prostokata(bok_a,bok_b))

    elif(wybor == 2):
        bok_k = int(input("Podaj dlugosc boku kwadratu: "))
        if(bok_k <= 0):
            print("zle dlugosci bokow")
            continue
        print(pole_kwadratu(bok_k))

    elif(wybor == 3):
        bok_c = int(input("Podaj dlugosc podstawy trojkata: "))
        h_c = int(input("Podaj dlugosc wysokosci trojkata: "))
        if(bok_c <= 0) | (h_c <= 0 ):
            print("zle dlugosci odcinkow")
            continue
        print(pole_trojkata(bok_c,h_c))

    elif(wybor == 4):
        bok_x = int(input("Podaj dlugosc pierwszej podstawy trapezu: "))
        bok_y = int(input("Podaj dlugosc drugiej podstawy trapezu: "))
        h_t = int(input("Podaj dlugosc wysokosci trapezu: "))
        if(bok_x <= 0) | (h_t <= 0 ) | (bok_y <= 0 ):
            print("zle dlugosci odcinkow")
            continue
        print(pole_trapezu(bok_x,bok_y,h_t))

    elif(wybor == 5):
        r = int(input("Podaj dlugosc promienia kola: "))
        if(r <= 0):
            print("zla dlugosc promienia")
            continue
        print(pole_kola(r))

    elif(wybor == 6):
        x=False
        
    else:
        print("error")
        continue
        


        
