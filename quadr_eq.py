import math
import cmath

def viet(b,c):
    if (b == 0) and (c == 0):
        x1 = 0
        x2 = 0
    else:
        d = b**2 - 4*c
        if d >= 0:
            sqd = math.sqrt(d)
        else:
            sqd = cmath.sqrt(d)
        if b>= 0:
            x1 = (-b - sqd) / 2.0
        else:
            x1 = (-b + sqd) / 2.0
        x2 = c/x1
    return x1, x2

def tailor(b,c):
    a = 4*c/b**2
    if a**2  < 10**-25:
        x1 = - 1.0 * c / b + 2 * c / b ** 3
        x2 = -b * 1.0
    else:
        x1,x2 = viet (b,c)
    return x1, x2 

print(viet(2,1))
print(tailor(2,1))
