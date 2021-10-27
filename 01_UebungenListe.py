#
# Name: Phillip Ahlers 
# Datum:  28.10.2021
# Klasse: ETS2021
#
# Version: 1.0.0 
# Aufgabe: Übungen Listen
#
#
#


'''''''''''''''''''''''''''''''''''
Definieren der Liste
'''''''''''''''''''''''''''''''''''

namen = ["Werner","Udo", "Herbert", "Silke", "Claudia", "Kai", "Kerstin", "Elke", "Toni", "Christina", "Anna", "Ute", "Klaus", "Britta", "Katja", "Simone", "Claus", "Tim", "Theodor"]

'''''''''''''''''''''''''''''''''''
Ausgabe der Liste:
'''''''''''''''''''''''''''''''''''

print("Namen in der Liste:")
for i in range(len(namen)):
    print(namen[i], end=" ")
print("\n")



'''''''''''''''''''''''''''''''''''
Ausgabe in umgekehrter Reihenfolge:
'''''''''''''''''''''''''''''''''''

print("Umgekehrte Reihenfolge:")
for i in range(len(namen)):
    print(namen[len(namen)-1-i], end=" ")
print("\n")



'''''''''''''''''''''''''''''''''''
Austauschen Christina --> Christine
'''''''''''''''''''''''''''''''''''

print("Austauschen Christina --> Christine")
for i in range(len(namen)):
    if namen[i] == "Christina":
        namen[i] = "Christine"
    print(namen[i], end=" ")
print("\n")



'''''''''''''''''''''''''''''''''''
Hinzufügen von Andrea, Andi und Wolfgang
'''''''''''''''''''''''''''''''''''

print("Hinzufügen von Andrea, Andi und Wolfgang")
neueNamen = ["Andrea", "Andi", "Wolfgang"]
namen.extend(neueNamen)
for i in range(len(namen)):
    print(namen[i], end=" ")
print("\n")


'''''''''''''''''''''''''''''''''''
Sortieren der Liste in Alphabetischer Reihenfolge:
'''''''''''''''''''''''''''''''''''

print("Sortieren der Liste von A-Z:")
namen.sort()
for i in range(len(namen)):
    print(namen[i] , end=" ")
print("\n")



'''''''''''''''''''''''''''''''''''
Sortieren der Liste entgegen Alphabetischer Reihenfolge:
'''''''''''''''''''''''''''''''''''

print("Sortieren der Liste von Z-A")
namen.sort(reverse=True)
for i in range(len(namen)):
    print(namen[i], end=" ")
print("\n")



'''''''''''''''''''''''''''''''''''
Länge der Liste ermitteln
'''''''''''''''''''''''''''''''''''
print("Die Liste hat", end=" ")
print(len(namen), end=" ")
print("Eingräge")
