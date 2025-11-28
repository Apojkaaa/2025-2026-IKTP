import random


szoveg = input("Adjon meg egy szöveget: ")
betu = input ("Adjon meg egy betűt:")

index = 0
while(index < len(szoveg) and  szoveg[index] != betu):
    #index = index + 1
    index += 1
print(index)

if(index < len(szoveg)):
    #for index in range(0,len(szoveg),1):
    db = 0
    for karakter in szoveg:
        if(karakter == betu):
            db+=1
    print(db)
else:
    print("Nincs az adott betű a szövegben")