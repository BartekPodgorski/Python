"""
plytka kopia / list(na list ) / [:]
def evil_function(toBeDestroyedList):
    toBeDestroyedList.clear()

myList = [1,4,2,1,52,3]

evil_function(myList.copy())

"""
#nie zabezpieczylismy sie przed zmianami wewnatrz elementow listy
#deepcopy
import copy

def evil_function(toBeDestroyedList):
    toBeDestroyedList[0][0]=20

myList = [[1,4],[2,1],[52,3]]

evil_function(copy.deepcopy(myList))
