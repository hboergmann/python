import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
        
grid1 = [[9, 0, 0, 0, 7, 0, 0, 0, 4],
         [0, 1, 0, 0, 0, 0, 0, 5, 0],
         [0, 0, 8, 0, 0, 0, 2, 0, 0],
         [0, 0, 0, 8, 0, 9, 0, 0, 0],
         [7, 0, 0, 0, 4, 0, 0, 0, 6],
         [0, 0, 0, 2, 0, 7, 0, 0, 0],
         [0, 0, 3, 0, 0, 0, 1, 0, 0],
         [0, 2, 0, 0, 0, 0, 0, 8, 0],
         [6, 0, 0, 0, 9, 0, 0, 0, 7]]

grid2 = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
         [3, 0, 4, 0, 0, 0, 7, 0, 1],
         [1, 5, 0, 0, 0, 0, 0, 3, 4],
         [0, 1, 0, 7, 9, 2, 0, 8, 0],
         [5, 0, 0, 1, 0, 6, 0, 0, 7],
         [0, 4, 0, 8, 5, 3, 0, 9, 0],
         [7, 6, 0, 0, 0, 0, 0, 4, 8],
         [4, 0, 8, 0, 0, 0, 5, 0, 9],
         [0, 0, 0, 0, 7, 0, 0, 0, 0]]

# Funktion prüft, in der Reihe oder Spalte oder 
# im 3 mal 3 Quadrat die Ziffer n schon vorhanden ist
def possible(y, x, n):
    global grid
    # Ziffer n in Zeile schon vorhanden
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    # Ziffer n in Spalte schon vorhanden
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    # Null Koordinaten des 3 mal 3 Quadrats ermitteln
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    # Ziffer n im Quadrat vorhanden
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False    # Ziffer enthalten
    return True                 # Ziffer nicht enthalten

# Funktion prüft jedes Feld, ob Ziffer n passt
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:             # Zelle nicht belegt
                for n in range(1, 10):
                    if possible(y, x, n):   # ist n schon vergeben?
                        grid[y][x] = n      # Zelle mit n belegen
                        solve()             # erneuter Aufruf (rekursion)
                        grid[y][x] = 0      # keine Ziffer gefunden
                return                      # Rücksprung
    print(np.matrix(grid))                  # 1. Lösung ausgeben
    input("More?")                          # Weitere Lösungen suchen

# print(np.matrix(grid))
print()
solve()



