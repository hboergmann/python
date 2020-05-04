# ägyptischer_bruch (nach Fibonachi)
# jeder beliebige bruch läßt such aus der Summe von Stammbrüchen darstellen
# siehe auch Bleicher
from fractions import Fraction
def greedy(x,forceOdd = False):
    L = []

    print(str(x)+ " = ", end="")
    while x>0:
        inv = Fraction(1)/x
        u=int(inv)
        if u < inv:
            u += 1
        if forceOdd and u % 2 == 0:
            u += 1
            
        f = Fraction(1, u)
        
        L.append(f)
        x -= f
    print(" + ".join(map(str, L)))

greedy(Fraction(20, 21))
greedy(Fraction(5, 121))
greedy(Fraction(13, 71))



