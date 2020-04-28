# Primzahlen prüfen
from math import sqrt
# Calculates all prime factors of the given integer.
"""
Die Grund-Idee vond iesem Algorithmus liegt darin, dass eine Zahl keinen 
Primzahl-Faktor haben kann, der größer ist als die Quadratwurzel dieserZahl.
Für 𝑛 =  100 ist beispielsweise √100 = 10 der größtmögliche Faktor, der eine Primzahl sein könnte.
"""
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

# Beispiel
n = 2017
if len(prim(n)) == 1:
    print(str(n) + " ist eine Primzahl!")
else:
    print(str(n) +" ist k e i n e  Primzahl! " + str(n)+str(prim(n)))
print()
# Zahlenbereich in Primfaktoren zerlegen: 
for n in range(1, 1000):
    if len(prim(n)) == 1:
        print("n = " + str(n))
