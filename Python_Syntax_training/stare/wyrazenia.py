'''
liczby = [1,2,3,4,5,6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

print(potegiDwojki)
'''
#wyrazenie listowne []
'''
potegi2 = [element**2
           for element in range (0,20)
           ]

print(potegi2)

parzyste = [element
            for element in liczby
            if (element %2 ==0)
            ]

'''
#wyrazenie generujace () generuje na bierzaco malo pamieci
import sys

"""parzyste_generowane = (element
            for element in range(4400)
            if (element %2 ==0)
            )

parzyste = [element
            for element in range(4400)
            if (element %2 ==0)
            ]
print(sys.getsizeof(parzyste))
print(sys.getsizeof(parzyste_generowane))

for item in parzyste_generowane:
    print(item)

potega2 = (element **2
           for element in range(100)
           )

print(sum(potega2))

"""

#wyrazenia slownikowe {} mowimy co ma sie stac z kluczem i wartoscia
"""
names = {"Arek","Wiola","Karol","Bartek","Jakub"}
liczby = [1,2,3,4,5,6]
celsius ={"t1": -20,"t2":-15,"t3":0,"t4":12,"t5":24}

namesLenght = {
    name:len(name)
    for name in names
    if name.startswith("A") & name.endswith("k")
    }

multi ={
    liczba:liczba*liczba
    for liczba in liczby
    }

farenheit ={
    key:value*1.8 + 32
    for key,value in celsius.items()
    if value> -5 & value <20
    }
"""
#wyrazenia zbioru {} nie ma key 
"""
names = {"arek","wiola","Karol","bartek","Jakub"}

names = {
        name.capitalize()
        for name in names
        if name.startswith("b") | name.startswith("B")
        }
"""
#zad range(100,471) dzielone przez 7 i przez 5

generator = (
        element
        for element in range(100,471)
        if(element % 7 == 0) & (element % 5 !=0)
    )
for item in generator:
    print(item)
