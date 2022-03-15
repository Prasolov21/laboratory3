import math
xc=1
xf=0.9
e=0.0000217
r=100
while r>e:
    xp=xc
    xc=xf
    y=(2*xc)-math.log(xc + 2)
    d=(2* xp)-math.log(xp + 2)
    xf=xc-(((xc-xp)*y)/(y-d))
    g=(2*xf)-math.log(xf+2)
    r=abs(y-g)
    print(xf)