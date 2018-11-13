def karatsuba(x,y):
    n = len(x)
    if n==1:
        return int(x)*int(y)
    else:

        a,b = x[0:int(n/2)],x[int(n/2):]
        p = int(a)+int(b)
        c,d = y[0:int(n/2)],y[int(n/2):]
        q = int(c)+int(d)
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        pq = karatsuba(p,q)

        adbc = pq-ac-bd
        return 10^int(n) * ac + 10^int(n/2) * adbc + bd
        # return

x = str(1234)
y = str(5678)

result = karatsuba(x,y)
# print(result)
