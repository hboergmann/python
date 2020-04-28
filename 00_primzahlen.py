# Primzahlen prüfen
from math import sqrt
# Calculates all prime factors of the given integer.

def prim(n):
    pfactors = []
    limit = int(sqrt(n)) + 1
    check = 2
    num = n
    if n == 1:
        return [1]

    for check in range(2, limit):
      while num % check == 0:
        pfactors.append(check)
        num /= check

    if num > 1:
        pfactors.append(num)

    return pfactors


 # Einzelne Zahl in Primfaktoren zerlegen
 
 #print("Ist 2017 eine Primzahl: ")
 n = 2017
 prim(n)
 
 # Zahlenbereich in Primfaktoren zerlegen:
 for n in range(1,1000):
    print(prim(n))
