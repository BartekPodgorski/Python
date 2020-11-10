#mierzenie wydajnosci kodu
import time
#Dodawanie za pomoca petli
def sumuj_do(liczba):
    suma = 0
    for liczba in range (liczba+1):
        suma = suma + liczba
    return (suma)
#dodawanie za pomoca wyrazenia generujacego
def sumuj_do2(liczba):
    return sum((liczba for liczba in range(liczba+1)))
#dodawanie za pomoca wyrazenia slownikowego    
def sumuj_do3(liczba):
    return sum({liczba for liczba in range(liczba+1)})
#dodawanie za pomoca wyrazenia listowego    
def sumuj_do4(liczba):
    return sum([liczba for liczba in range(liczba+1)])
    
#dodawanie za pomoca wlsnego liczeni
def sumuj_do5(liczba):
    return((1+liczba)/2*liczba)

def function_performance(func, arg, how_many_times = 1):
    suma = 0
    for i in range(0, how_many_times):        
        start=time.perf_counter()
        func(arg)
        end=time.perf_counter()
        suma = suma + (end-start)
    return suma/how_many_times


print(function_performance(sumuj_do,10000000))
print(function_performance(sumuj_do,10000000,6))
"""
print(function_performance(sumuj_do2,10000000))
print(function_performance(sumuj_do3,10000000))
print(function_performance(sumuj_do4,10000000))
print(function_performance(sumuj_do5,10000000))
"""    


