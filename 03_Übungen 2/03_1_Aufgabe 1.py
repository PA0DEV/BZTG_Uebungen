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
teiler = 9          #Zahl durch die das Ergebnis ganzzahlig Teilbar sein soll
minZahl = 10         #Erste geprüfte Zahl
maxZahl = 100       #Letzte geprüfte Zahl



#for-Schleife zum testen aller Zahlen im parametrierten Bereich
for i in range(minZahl, maxZahl - minZahl + 1):
    if i % teiler == 0:        #Prüfung ob die Zahl durch den Teiler teilbar ist
        #Wenn ja, füge die Zahl zu der Liste der Ergebnisse hinzu
        zahlen.append(i)

print("Folgende Zahen sind zwischen", minZahl, "und", maxZahl, "durch", teiler, "teilbar:", zahlen)