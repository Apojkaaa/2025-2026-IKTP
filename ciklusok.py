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
import random


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
print()
#30-50ig 4el osztható számok
for elem in range(32,50,4):
    print (elem,end=" ")
print()

#10 től 1 ig a számok visszafele
for b in range(10,0,-1):
    print(b,end=" ")
print()

for index in range(len(szoveg)-1, -1, -1):
    print(szoveg[index],end="")
print()
 
#irassa ki a szöveget az helyével társítva
#be: kalapács
# ki: 1k 2a 3l 4a 5p 6á 7c 8s
n = len(szoveg)
for index in range (0, n, 1):
    print(str(index+1)+szoveg[index], end=" ")

# írasson ki 5 db véletlen karaktert a szövegből

for db in range(0,5,1):
    szam =random.randint(0,n-1)
    print(szoveg[szam],end=" ")
print("")
ujszoveg =" "
for index in range(-1, -n-1, -1):
    ujszoveg += szoveg[index]
print(ujszoveg)
#hf 17-21