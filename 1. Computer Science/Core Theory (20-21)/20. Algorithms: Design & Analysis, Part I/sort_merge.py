from lib.merge import merge
def msort(array):
    n = len(array)
    if len(array)<2:
        return array
    else:
        array_A = array[0:n//2]
        array_B = array[n//2:]
        sort_A = msort(array_A)
        sort_B = msort(array_B)
        sorted_array = merge(sort_A,sort_B)
        return sorted_array

sort = input("array=").split(',')
sort = [int(x) for x in sort] 
nam = msort(sort)
print(nam)
