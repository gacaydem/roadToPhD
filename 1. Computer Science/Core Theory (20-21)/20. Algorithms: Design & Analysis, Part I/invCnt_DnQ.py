def merge(array_a,array_b):
    i = 0
    j = 0
    result = []
    num_remain = 0
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
            num_remain+= len(array_a)-i
        
    return result, num_remain

def dnqInvCnt(arr):
    n = len(arr)
    if n<=1:
        return arr,0
    else:
        arr_a = arr[0:n//2]
        arr_b = arr[n//2:]
        
        sort_a,inv_a = dnqInvCnt(arr_a)
        sort_b,inv_b = dnqInvCnt(arr_b)
        sorted_array, split_inv = merge(sort_a,sort_b)
        total_inv = inv_a + inv_b + split_inv

    return sorted_array,total_inv
    
num = input("array=").split(',')
num = [int(x) for x in num] 
nam = dnqInvCnt(num)
print(nam)