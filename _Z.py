# wie viele versuche braucht es, 
# um eine Summe > 1 aus Zufallszahlen von 0 bis 1 zu erzeugen ==> e

from random import random
def Z():
    s = 0
    c = 0
    while s < 1:
        c += 1
        s += random()
    return c
    
def test(n):
    return sum(Z() for i in range(n)) / n


print(test(10000000))




