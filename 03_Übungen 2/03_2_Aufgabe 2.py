#
# Name: Phillip Ahlers 
# Datum:  12.11.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe: 
# Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe und einem
# bestimmten Zinssatz monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.
import math

kreditsumme = 200000        #Gesamtsumme des Kredites in €
zinssatz = 0.03             #Zinssatz zu dem der Kredit gewährt wurde in dezimal
dauer = 20                 #Laufzeit des Kredites in Jahren

#Berechnung der Monatlichen Rate um nach der Laufzeit Schuldenfrei zu sein
#formel nach https://www.finanzen-rechner.net/kredit/monatsrate-berechnen.html (16.11.2021)
rate = round(kreditsumme * (zinssatz/12)/(1-(1+zinssatz/12)**(-dauer *12)), 2)

#Ausgabe der Monatlichen Rate
print("Monatliche Rate um schuldenfrei zu sein beträgt %f €" %rate)
