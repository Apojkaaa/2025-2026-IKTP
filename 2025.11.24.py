import random

gondolt_szam =random.randint(10,99)

print("Melyik kétjegyű számra goonolok")
szam =int(input("Szám: "))
if(szam >gondolt_szam):
    print("A szám nagyobb mint a gondolt szám.")

while(szam !=gondolt_szam):
    if(szam > gondolt_szam):
        print("A szám nagyobb mint a gondolt szám")
    elif(szam < gondolt_szam):
        print("A szám kisebb mint a gondolt szám")
    else:
        print("Eltaláltad")
    szam = int(input("Probálkozz még egyszer: "))