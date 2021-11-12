#
# Name: Phillip Ahlers 
# Datum:  12.11.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe: 
# Schreiben Sie ein Programm, das mithilfe einer for-Schleife alle durch 9 teilbaren Zahlen zwischen zwei zuvor eingegebenen 
# Grenzen in eine Liste schreibt und
# dann ausgibt.

zahlen = []
teiler = 9
minZahl = 0
maxZahl = 100

for i in range(maxZahl - minZahl + 1):
    if i % teiler == 0:
        zahlen.append(i)

print("Folgende Zahen sind zwischen", minZahl, "und", maxZahl, "durch", teiler, "teilbar:", zahlen)