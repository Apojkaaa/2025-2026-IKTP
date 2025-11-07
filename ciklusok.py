"""
Ciklusok - ismétlés - loop

Számlálós - For ciklus
Végig megy a megadott elemeken vagy intervallumon!
for elem in range (mettől, meddig, hányasával):
    Ismétlendő folyamat

    for karakter in szoveg:
        Ismétlődő folyamat


Tesztelős - While

"""

#1[1,10]ig a  számok

for elem in range(1,11,1):
    print(elem,end=" ")

print()

#első 10db páros szám

for elem in range(0,19,2):
    print(elem,end=" ")

#Szöveg betűi közé vesszőt
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter,end=",")

