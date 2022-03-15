#так как функция не сходится, посчитать методом иттераций не возможно
x=2
e=0.00001
b=True
n=0
while b==True:
    y=x**3-2.92*x**2+1.4355*x+0.791136
    if abs(x-y)<e:
        b=False
    x=y
    n=n+1
    if n==100: break
    print(x)