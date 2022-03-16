import math
x1=1
x2=0.9
e=0.0000217
r=100
while r>e:
    x0=x1
    x1=x2
    y=(2*x1)-math.log(x1 + 2)
    d=(2* x0)-math.log(x0 + 2)
    x2=x1-(((x1-x0)*y)/(y-d))
    g=(2*x2)-math.log(x2+2)
    r=abs(y-g)
    print(xf)
