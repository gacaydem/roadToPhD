from lib.swap import swap
def bsort(array):
    n = len(array)
    while True:
        array_tmp = array[:]
        for i in range(n-1):
            if array[i]>=array[i+1]:
                array[i],array[i+1] = swap(array[i],array[i+1])
        if array_tmp == array:
            break
    return array

sort = input("array=").split(',')
sort = [int(x) for x in sort] 
nam = bsort(sort)
# nam = bsort([1,2,0])
print(nam)
    
            