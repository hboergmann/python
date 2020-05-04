#00_0_snake
import pygame as pg
import sys
import numpy as np


partikel = 25
schlange = [[13, 13], [13, 14]]
apfelCoords = []
richtung = 0  # 0: oben, 1:rechts, 2:unten, 3:links

pg.init()
clock = pg.time.Clock()
font = pg.font.SysFont('arialblack',35)
screen = pg.display.set_mode([700, 700])


def textObjekt(text, font):
    textFlaeche = font.render(text, True, (255, 255, 255))
    return textFlaeche, textFlaeche.get_rect()

def zeichner():
    screen.fill((0, 102, 0))

    for a in apfelCoords:
        Coords = [a[0] * partikel, a[1] * partikel]
        pg.draw.rect(screen, (255, 0, 0), (Coords[0], Coords[1], partikel, partikel), 0)
        
    kopf = True
    for x in schlange:
        Coords = [x[0] * partikel, x[1] * partikel]
        if kopf:
            pg.draw.rect(screen, (0, 0, 0), (Coords[0], Coords[1], partikel, partikel), 0)
            kopf = False
        else:
            pg.draw.rect(screen, (47, 79, 79), (Coords[0], Coords[1], partikel, partikel), 0)

def apfelCoordGen():
    notOK = True
    while notOK:
        Coord = [np.random.randint(0, 28), np.random.randint(0, 28)]
        change = False
        for x in schlange:
            if Coord == x:
                change == True
        for x in apfelCoords:
            if Coord == x:
                change = True
        if change == False:
            return Coord

apfelCoords.append(apfelCoordGen())

go = True
anhang = None
apfelInd = -1
ende = False
score = 0
leben = 6

while go:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and richtung != 2:
                richtung = 0
            if event.key == pg.K_RIGHT and richtung != 3:
                richtung = 1   
            if event.key == pg.K_DOWN and richtung != 0:
                richtung = 2
            if event.key == pg.K_LEFT and richtung != 1:
                richtung = 3
    if anhang != None:
        schlange.append(anhang.copy())
        anhang = None
        apfelCoords.pop(apfelInd)
               
    zahl = len(schlange) - 1
    for i in range(1, len(schlange)):
        schlange[zahl] = schlange[zahl - 1].copy()
        zahl -= 1
        
    if richtung == 0:
        schlange[0][1] -= 1
    if richtung == 1:
        schlange[0][0] += 1
    if richtung == 2:
        schlange[0][1] += 1
    if richtung == 3:
        schlange[0][0] -= 1

    for x in range(1, len(schlange)):
        if schlange[0] == schlange[x]:
            ende = True
    if schlange[0][0] < 0 or schlange[0][0] > 27:   # links oder rechts raus
        ende = True
    if schlange[0][1] < 0 or schlange[0][1] > 27:   # oben oder unten raus
        ende = True       

    for x in range(0, len(apfelCoords)):
        if apfelCoords[x] == schlange[0]:  
            anhang = schlange[-1].copy()
            apfelInd = x
            score += 10
        
    zufall = np.random.randint(0, 100)
    if zufall <= 1 and len(apfelCoords) < 4 or len(apfelCoords) == 0:
        apfelCoords.append(apfelCoordGen())

    if ende == False:
        zeichner()
        text = "Score: " + str(score) + " - "
        text1 = "Leben: " + str(leben)
        textGrund, textKasten = textObjekt(text + text1, font)
        textKasten.center = ((350, 40))
        screen.blit(textGrund, textKasten)
        pg.display.update()
    else:
        print("Du hast " + str(score) + " Punkte erreicht")
        leben -= 1

        if leben == 0:
            sys.exit()
        else:
            schlange = [[13, 13], [13, 14]]
            apfelCoords = []
            richtung = 0  # 0: oben, 1:rechts, 2:unten, 3:links
            go = True
            anhang = None
            apfelInd = -1
            ende = False
            score = 0
    
    clock.tick(8)