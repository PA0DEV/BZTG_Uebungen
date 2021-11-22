#
# Name: Phillip Ahlers 
# Datum:  13.11.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe: 
# Ermitteln Sie für einen festgelegten Zahlenbereich die Primzahlen und schreiben sie diese 
# in eine Liste. Geben Sie die Liste anschließend aus.
# 

import math

primZahlen = []
teiler =[]

minZahl = 10         # Erste zu prüfende Zahl (mindestens 2)
maxZahl = 1000       # Letzte zu überprüfende Zahl


if minZahl < 2:
    exit("[ERROR] Min zahl muss mindestens 2 sein!")

for i in range(2, maxZahl+1):
    teiler.append(i)

for j in range(minZahl, maxZahl+1):   #
    isPrim = True                   # flag Primzahl
    for number in teiler:       # prüfen duch teilen mit allen bisher gefundenen Primzahlen
        if j % number == 0:
            isPrim = False          # Wenn zahl ganzzahlig Teilbar, dann setze flag --> 0 und beende die überprüfung
            break
    if isPrim:                      # Wenn die Flag noch True ist nach der prüfung,
        primZahlen.append(i)        # füge Zahl der Liste hinzu

print("Liste der Primzahlen bis", maxZahl, "\n", primZahlen)

