# Josephus Problem
# Eine Anzahl Spieler sitzt im Kreis. Der erste Spieler "schubst" den rechten Mitspieler raus.
# Der nächste schubst wieder seinen rechten Nachbar raus, usu, usw 
# bis zum Schluss einer übrig bleibt

import pygame as pg
import math
import time

total = 34          # Gesamtanzahl Personen
faktor = 0
winkelschritt = math.tau / total
breite, höhe = 600, 600
zentrum = (breite//2, höhe//2)
zx, zy = zentrum
radius = breite//2-16

felder = []
global feld

# Ein oder mehrere Felder weiterrücken, bis man auf nicht ausgeschiedenen Partner trifft
def feld_plus(feld):
    feld = feld + 1
    if(feld == total):
        feld = 0
    return feld

while total > 4:
    # array mit ziffern 1 bis total füllen
    felder = []
    for i in range(total):  # felder mit Zahlen 1 bis total füllen
        felder.append(i + 1)
    # main: bei 1 beginnend schubst man seinen rechten partner raus, bis nur der letzte übrig bleibt
    feld = 0
    weitermachen = True
    while (weitermachen):
        z = 1   # Zähler für maximale Anzahl Mitspieler (total)
        while(felder[feld] == 0 and z < total):
            feld = feld_plus(feld)  # nächstes feld, welcher nicht leer (Schubser)
            z = z + 1
        if z == total:
            weitermachen = False    # Spielende, wenn keiner gefunden wird
        feld_schwert = feld
        feld = feld_plus(feld)      #  nächstes feld
        z = 1
        while(felder[feld] == 0 and z < total):
            feld = feld_plus(feld)  # nächstes feld, welches nicht leer (fliegt raus)
            z = z + 1
        if z == total:
            weitermachen = False    # keiner mehr da
        if weitermachen:        
            felder[feld] = 0        # spieler fliegt raus
    print("Anzahl: " + str(total) + ": " + str(feld + 1) + " - " + str(felder))
    total = total - 1
    

