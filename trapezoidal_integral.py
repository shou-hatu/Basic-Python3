from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
#(1)
def f(x):
    return (sin(x))
def trintegral(a = 0,b = 1,n = 100):
    h = (b - a) / n
    count = 1
    terms = []
    #for文で初項からn項までリストに入れる
    for count in range(1,(n + 1)):   
        term = (h / 2)*((f(a + (count - 1)* h) + f(a + count * h)))
        terms.append(term)
       
    #リストに入れた項の総和を出す(sum関数を使った方が楽！)
    #sum(list)でlistの総和を出せる！
    #print(sum(list))で合計表示できる！
    return(sum(terms))
print('(1){}'.format(trintegral(0,((math.pi) / 2),50)))
#(2)
def f(x):
    return 4/(1 + (x**2))
print('(2){}'.format(trintegral(0,1,100)))
#(3)
def f(x):
    return math.pi ** (1 / 2) * math.exp(- x ** 2)
print('(3){}'.format(trintegral(-100,100,1000)))