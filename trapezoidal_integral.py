from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
h = ( math.pi*(1/2)- 0)/ 100
count = 1

#while文で初項から100項までリストに入れる
while count <= 100:
    terms = []
    terms.append((h / 2)*((sin(0 + (count - 1)* h) + sin(0 + count * h))))
    count += 1
    if count > 100:
        break
print(terms)

#リストに入れた項の総和を出す
def sygma(terms):
    s = 0
    for i in range (0, len(terms)):
        s = s + terms[i]
        return s
print(sygma(terms))
    
        