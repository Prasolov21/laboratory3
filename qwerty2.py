import math
a=0
b=1
e=0.00001
fa=math.sin(a)-math.cos(a)
fb=math.sin(b)-math.cos(b)
fx=fa
while abs(b-a)>e:
    x=(a+b)/2
    y=math.sin(x)-math.cos(x)
    if (y*fx)<0:
       b=x
       fb=fx
    else:
        a=x
        fa=fx
    print(x)