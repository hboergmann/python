# Josephus Problem
# Josephus Problem
# Eine Anzahl Spieler sitzt im Kreis. Der erste Spieler "schubst" den rechten Mitspieler raus.
# Der nächste schubst wieder seinen rechten Nachbar raus, usu, usw 
# bis zum Schluss einer übrig bleibt

import pygame as pg
import math
import time

TOTAL = total = 41         # Gesamtanzahl Personen
faktor = 0
schwert = 0
winkelschritt = math.tau / total
breite, höhe = 600, 600
zentrum = (breite//2, höhe//2)
zx, zy = zentrum
radius = breite // 2 - 16

global feld
felder = []

# Berechnet die Koordinaten der Kreispunkte (Spieler)
def i2Pos(i):
  winkel = winkelschritt * i + math.pi      # math.pi = 90°
  x = int(zx + radius * math.cos(winkel))   # zx, zy ==> Zentrum
  y = int(zy + radius * math.sin(winkel))
  return (x,y)

# Ein oder mehrere Felder weiterrücken, bis man auf nicht ausgeschiedenen Partner trifft
def feld_plus(feld):
    feld = feld + 1
    if(feld == total):
        feld = 0
    return feld

# array mit ziffern 1 bis total füllen
for i in range(total):  # felder mit Zahlen 1 bis total füllen
    felder.append(i + 1)

# screen initialisieren
pg.init()
screen = pg.display.set_mode((breite, höhe))
screen2 = pg.Surface((breite,höhe))
farbe = pg.Color(150,150,150)

# zeichne kreis
pg.draw.circle(screen2, (255, 255, 255), zentrum, radius, 2)  # zeichne Kreis mit r = radius

# startpunkte auf dem Kreis berechnen und einzeichnen
startpunkte = []
for punkt in range(TOTAL):
    pos = i2Pos(punkt)
    startpunkte.append(pos)
    if felder[punkt] == 0:
        pg.draw.circle(screen2, (250, 0, 0), pos, 6)  # rote Punkte auf dem Kreis
    else:
        pg.draw.circle(screen2, (0, 250, 0), pos, 6)  # grüne Punkte auf dem Kreis

screen.blit(screen2, (0, 0))
pg.display.flip()

print("Spieler : " + str(punkt) + "Koordinaten: " + str(startpunkte))
     
feld = 0
clock = pg.time.Clock()
weitermachen = weiter = True
while weitermachen:
    clock.tick(50000)
    for event in pg.event.get():
        if event.type == pg.QUIT or \
            (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            weitermachen = False
    
    # screen.blit(screen2,(0,0))
    # main: bei 1 beginnend schubst man seinen rechten partner raus, bis nur der letzte übrig bleibt
    z = 1   # Zähler für maximale Anzahl Mitspieler (total)
    while(felder[feld] == 0 and z < total):
        feld = feld_plus(feld)  # nächstes feld, welcher nicht leer (Schubser)
        z = z + 1
        
    if z == total:
        weitermachen = False    # Spielende, wenn keiner gefunden wird
    schwert = feld + 1
    feld = feld_plus(feld)      #  nächstes feld
    z = 1
    while(felder[feld] == 0 and z < total):
        feld = feld_plus(feld)  # nächstes feld, welches nicht leer (fliegt raus)
        z = z + 1
    if z == total:
        weitermachen = False    # keiner mehr da
    if weitermachen:        
        felder[feld] = 0  # spieler fliegt raus
        print(felder)
    
        pos = i2Pos(feld)
        print(pos)
        pg.draw.circle(screen2, (250, 0, 0), pos, 6)  # rote Punkte auf dem Kreis
        screen.blit(screen2,(0,0))
        
        farbe.hsva = (100,100,100)
        screen3 = pg.font.SysFont('cour',82).render(f'{(schwert):6.1f}',False,(farbe))
        screen.blit(screen3,(200,250))

        pg.display.flip()
        x = 0
        while x < 1:
            # text_ausgabe.insert("end",".")
            time.sleep(1)
            x += 1
    
Eingabe = input("Enter für weiter!")
# pg.quit()

  