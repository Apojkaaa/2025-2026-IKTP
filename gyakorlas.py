#kérjen be egy szöveget és egy betűt
#nézze meg van e szövegben az adott betű 
#adja meg hány darab betű van a szövegben


szoveg = input("adjon meg egy szöveget: ")
betu = input("adjon meg egy betűt: ")
db = 0
for karakter in szoveg:
    if(karakter == betu):
        db+=1
print(db)

index = 0
while(index < len(szoveg)szoveg[index] != betu):
    index += 1
print(index)