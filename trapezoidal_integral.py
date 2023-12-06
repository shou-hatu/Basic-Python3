from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

#(1)
def trintegral(f,a = 0,b = 1,n = 100):

    h = (b - a) / n
    count = 1
    terms = 0
    for count in range(1,(n + 1)):   
        term = (h / 2)*((f(a + (count - 1)* h) + f(a + count * h)))
        terms = terms + term
    return(terms)
print('(1){}'.format(trintegral(sin,0,((math.pi) / 2),50)))
#(2)
def fsecond(x):
    return 4/(1 + (x**2))
print('(2){}'.format(trintegral(fsecond,0,1,100)))
#(3)
def fthird(x):
    return math.pi ** (1 / 2) * math.exp(- x ** 2)
print('(3){}'.format(trintegral(fthird,-100,100,1000)))
