from lib.compare import compareArr
def isort(array):
    n = len(array)
    sorted_array = []
    sorted_array.append(array[0])
    for i in range(1,n):
        sorted_array = compareArr(sorted_array,array[i])

    return sorted_array

sort = input("array=").split(',')
sort = [int(x) for x in sort] 
nam = isort(sort)
print(nam)
