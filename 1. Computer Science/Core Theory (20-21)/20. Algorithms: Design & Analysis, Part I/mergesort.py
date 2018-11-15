def merge(array_a,array_b):
    i = 0
    j = 0
    result = []
    n = len(array_a+array_b)
    for k in range(n):
        if i >= len(array_a):
            for x in array_b[j:]:
                result.append(x)
            break
        if j >= len(array_b):
            for y in array_a[i:]:
                result.append(y)
            break
        if array_a[i]<array_b[j]:
            result.append(array_a[i])
            i+=1
        else:
            result.append(array_b[j])
            j+=1
        
    return result

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
