from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

import math

a = 0
b = math.pi / 2
n = 100

h = (b - a)/ n
count = 1
terms = []
#for文で初項から100項までリストに入れる
for count in range(1,(n + 1)):
    
    term = (h / 2)*((sin(a + (count - 1)* h) + sin(a + count * h)))
    
    terms.append(term)
#リストに入れた項の総和を出す(sum関数を使った方が楽！)
#sum(list)でlistの総和を出せる！
#print(sum(list))で合計表示できる！
print(sum(terms))
    
        