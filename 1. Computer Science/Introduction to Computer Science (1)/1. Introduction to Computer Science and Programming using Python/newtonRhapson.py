
y = float(input('y='))
x = float(y/2)
e = 0.001
count = 0
while abs(x**2 -y) > e:
    x-= (x**2-y)/(2*x)
    count+=1
    print('Predict number',count)
    print('x=',x)

print('\n >>>  Final Predict, x=',x,'with error <',e)
print(' >>>  Last assert: x=',round(x,2))


