def karatsuba(x,y):
    if x<10:
        return x*y
    else:
        n = int(len(str(x))/2)
        a,b = x//(10**n),x%(10**n)
        c,d = y//(10**n),y%(10**n)
        p = a+b
        q = c+d
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        pq = karatsuba(p,q)
        adbc = pq-ac-bd
        return (10**(2*n)) * ac + (10**n) * adbc + bd

x = int(input('x='))
y = int(input('y='))

result = karatsuba(x,y)
print('x*y=',result)
