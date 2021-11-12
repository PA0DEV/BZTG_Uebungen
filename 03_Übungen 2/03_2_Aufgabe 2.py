#
# Name: Phillip Ahlers 
# Datum:  12.11.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe: 
# Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe und einem
# bestimmten Zinssatz monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.

kreditsumme = 100000
zinssatz = 0.03
dauer = 10

rate = (kreditsumme * (1 + zinssatz) / dauer) / 12
print("Monatliche Rate um schuldenfrei zu sein beträgt %d €" %rate)
