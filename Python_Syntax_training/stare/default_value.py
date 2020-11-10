import time

def check_time(func,how_many_time=1,**arg):
    suma=0
    for i in range(0,how_many_time):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        suma= suma +(end-start)

    return suma/how_many_time

def find_number(x,container):
    if(x in container):
        return True
    else:
        return False
        



setContainer = {i for i in range(1,1000)}
listContainer = {i for i in range(1,1000)}

print(check_time(find_number,100000 ,x = 983 , container=setContainer))
print(check_time(find_number,100000 ,x = 983 ,container=listContainer ))

"""
Najpierw ida argumenty znane a dopiero potem nieznane .
jezeli jest jeden to arg
do nienznanych wielu uzywamy *
jezeli dodamy do nich klucze musimy dac **
"""
