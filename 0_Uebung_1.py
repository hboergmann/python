# Umrechnung m in cm, km
import subprocess
go = True
while go == True:
    subprocess.call("cls", shell=True)
    print("Gebensie eine Strecke in Meter ein, die umgerechnet werden soll!")
    invalid = True
    while invalid:
        try:
            eingabe = float(input())
            invalid = False
        except:
            print("Ungültige Eingabe! Versuchen Sie es erneut.")

print("Das sind: " + str(eingabe / 1000) + " Kilometer.")
print("Das sind: " + str(int(eingabe * 100)) + " Zentimeter.")
print("Das sind: " + str(int(eingabe * 1000)) + " Millimeter.")

print("Wollen Sie eine weitere zahl wandeln?")
print("1)Ja")
print("2)Nein")
try:
    eingabe2 = int(input())
    if eingabe2 == 1:
        subprocess.call("cls",shell=True)
    else:
        print("Okay, Programm wird beendet")
        go = False
        
except:
    print("Ungültige Eingabe - Programm wird geschlossen!")
    go = False

