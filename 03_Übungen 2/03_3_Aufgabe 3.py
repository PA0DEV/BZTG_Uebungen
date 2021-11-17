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

pruefZahlen = []
primZahlen = []
minZahl = 1         # Erste zu überprüfende Zahl
maxZahl = 1000       # Letzte zu überprüfende Zahl

for i in range(2, maxZahl+1):
    isPrim = True
    for number in primZahlen:
        if i % number == 0:
            isPrim = False
            break
    if isPrim:
        primZahlen.append(i)

print("Liste der Primzahlen zwischen", minZahl, "und", maxZahl, "\n", primZahlen)

