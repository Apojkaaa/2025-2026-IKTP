import random
"""

Elől tesztelős ciklus
while ciklus

-nem tudjuk hányszor fog lefutni 
.feltételhez kötött
-akor ismétel ha a feltétel igaz

while(feltétel)
    utasítások(szekvencia)
"""

# generáljon véletlen számokat [0,10] között amíg nullát nem kapunk

velszam = random.randint(0,10)
print(velszam, end=" ")
while (velszam !=0):
    velszam = random.randint(0,10)
    print(velszam, end=" ")

#kérjen be számokat,addig ameddig 0 nem adnak meg
osszeg = 0
db = 0
szam = int(input("adjon meg egy számot: "))
while (szam !=0):
    osszeg +=szam
    db += 1
    szam =int(input("Adjon meg egy másikat: "))
print(round(osszeg/db,2))
#adott egy szöveg. Adja meg hogy van e benne x betű

szöveg = fauivfoavcvafibaijvixghhfaggrh
while(szöveg !=x):
    print(szöveg)


#hf ez+ 29 es feladatig minden