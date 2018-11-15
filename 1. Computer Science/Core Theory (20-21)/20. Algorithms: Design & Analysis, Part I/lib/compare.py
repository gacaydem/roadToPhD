def compare(a,b):
        if a>=b:
            return b
        else:
            return a

def compareArr(array,b):
    # n = len(array)
    flag = 0
    if b>=array[-1]:
        array.append(b)
        return array
    else:
        array_rem = array[0:-1]
        array_tmp = array[-1-flag:]
        flag += 1
        result_array = compareArr(array_rem,b)
        for i in array_tmp:
            result_array.append(i)
        return result_array