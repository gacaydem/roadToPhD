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