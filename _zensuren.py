import math
punkte = (17, 13, 18, 16, 14, 15, 14, 17, 16, 8, 11, 18, 7, 10, 16, 22)
x_mittel = sum(punkte) / len(punkte)
print(x_mittel)
s_quadrat = 0
anz = len(punkte)
print(str(anz))
for i in range(anz):
    s_quadrat = s_quadrat + (punkte[i] - x_mittel)** 2
s_quadrat = s_quadrat / (anz - 1)
s = math.sqrt(s_quadrat)

print(s)

zensur = []
for i in range(anz):
    # print(punkte[i])
    if punkte[i] > (x_mittel + 3 / 2 * s):
        zensur.append(1)
    else:
        if punkte[i] > (x_mittel + 1/ 2 * s):
            zensur.append(2)
        else:
            if punkte[i] > (x_mittel - 1 / 2 * s):
                zensur.append(3)
            else:
                if punkte[i] > (x_mittel - 3 / 2 * s):
                    zensur.append(4)
                else:
                    zensur.append(5)
                    

for i in range(anz):
    print("Punkte: " + str(punkte[i]) + " ==> Zensur: " + str(zensur[i]))
