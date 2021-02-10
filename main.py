import math
def f(x,y):
    return (((x**3-y**6+80)/(y**5-5*y+89))+((math.log1p(y)-math.cos(x)+23)/(math.tan(y))+math.e**3)-(math.e**y-y**8-76))
x=int(input("Enter X: "))
y=int(input("Enter Y: "))
print ('%e' % f(x, y))