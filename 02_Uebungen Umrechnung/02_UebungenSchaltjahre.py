#
# Name: Phillip Ahlers 
# Datum:  5.11.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe 2: Schaltjahrberechnung
#
#
#


'''
Nummer 1:
Ist das gesuchte Jahr ein Schaltjahr?
'''

pruefJahr = 2021


if (pruefJahr % 4 == 0) and ((pruefJahr % 100 != 0) or (pruefJahr % 400 == 0)):     #Prüfung ob es ein Schaltjahr ist
    print(pruefJahr, "ist ein Schaltjahr")      #Ausgabe ist ein schaltjahr
else:
    print(pruefJahr, " ist kein Schaltjahr")    #Ausgabe ist kein Schaltjahr


'''
Nummer 2
Ausgabe aller Schaltjahre bis 5000 in einer Liste
'''
minJahr = 1800
maxJahr = 2300
listeSchaltjahre = []

for i in range(maxJahr - minJahr):
    jahr = i + minJahr
    if (jahr % 4 == 0) and ((jahr % 100 != 0) or (jahr % 400 == 0)):     #Prüfung ob es ein Schaltjahr ist
        listeSchaltjahre.append(jahr)

print("Liste der Schaltjahre zwischen", minJahr, "und", maxJahr, ":", listeSchaltjahre)
