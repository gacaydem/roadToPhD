from lib.findex import findex
from lib.swap import swap
from lib.fmin import fminop


def ssort(array):
    n = len(array)
    for i in range(n):
        minf = fminop(array[i:])
        ix = findex(array[i:],minf)
        array[i],array[ix+i]=swap(array[i],array[ix+i])
    
    return array
        
sort = input("array=").split(',')
sort = [int(x) for x in sort] 
nam = ssort(sort)
print(nam)