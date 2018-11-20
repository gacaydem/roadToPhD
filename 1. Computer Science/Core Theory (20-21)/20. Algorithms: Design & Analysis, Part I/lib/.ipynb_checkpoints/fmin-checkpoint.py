def compare(a,b):
        if a>=b:
            return b
        else:
            return a
            
def fmin(array): 
    minf = array[0]
    for i in array[1:]:
        if minf>i:
            minf = i
    return minf

def fminop(array):
    n = len(array)
    if n==1:
        return array[0]
    if n==2:
        return compare(array[0],array[1])
    else:
        array_A = array[0:n//2]
        array_B = array[n//2:]
        minf_A = fminop(array_A)
        minf_B = fminop(array_B)
        return compare(minf_A,minf_B)