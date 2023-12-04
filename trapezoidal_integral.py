from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

#(1)
def ffirst(x):
    return (sin(x))
def trintegral(a = 0,b = 1,n = 100):
    h = (b - a) / n
    count = 1
    terms = 0
    for count in range(1,(n + 1)):   
        term = (h / 2)*((ffirst(a + (count - 1)* h) + ffirst(a + count * h)))
        terms = terms + term
    return(terms)
print('(1){}'.format(trintegral(0,((math.pi) / 2),50)))
#(2)
def fsecond(x):
    return 4/(1 + (x**2))
def trintegral(a = 0,b = 1,n = 100):
    h = (b - a) / n
    count = 1
    terms = 0
    for count in range(1,(n + 1)):   
        term = (h / 2)*((fsecond(a + (count - 1)* h) + fsecond(a + count * h)))
        terms = terms + term
    return(terms)
print('(2){}'.format(trintegral(0,1,100)))
#(3)
def fthird(x):
    return math.pi ** (1 / 2) * math.exp(- x ** 2)
def trintegral(a = 0,b = 1,n = 100):
    h = (b - a) / n
    count = 1
    terms = 0
    for count in range(1,(n + 1)):   
        term = (h / 2)*((fthird(a + (count - 1)* h) + fthird(a + count * h)))
        terms = terms + term
    return(terms)
print('(3){}'.format(trintegral(-100,100,1000)))