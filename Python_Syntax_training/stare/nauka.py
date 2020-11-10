import random
from collections import Counter
nauka ={
    'python': 0.5,
    'film': 0.5
    }

list_nauka = list(nauka.keys())
list_nauka_values = list(nauka.values())
decyzja = []
i=0    
while True:
    x = random.choices(list_nauka,list_nauka_values)[0]
    decyzja.append(x)
    condiction = Counter(decyzja)
    if(condiction['python'] == 3): 
        print("win python")
        break
    elif(condiction['film'] == 3):
        print("we watch film")
        break
    
print(decyzja)    

