import random
"""
Függvények
(Chratch blokkok)

Előr definilált (megírtg, megfogalmazott) folyamatok, amik külső értéktől függetlenül végrehajtják a belső utasításokat

def fuggvenyNev():
    #Függvény tartalma

fuggvenynev() #függvény meghívása
"""
# visszatérés érték nélküli függvények - eljárás
#általában iyratás nélkül 
#osszeadas függvény definiálása 
def osszeadas():
    a = 12
    b =17
    print(a+b)
#összeadas klső értéktől függően paraméteren keresztül
def osszeadasParam(a,b):
    c = a + b
    print(c)
#összeadas függvény meghívása
osszeadas()
osszeadasParam(13,19)
# visszatéréssel rnedelkező függvények 
def kettoAtizediken():
    # a = math.pow(2,10)
    a = 2**10
    return a 
kettoAtizediken()
def osszeadasVisszateressel(a,b):
    c = a + b 
    return c 
print(osszeadasVisszateressel(13,17))

def veletlenszamkiiratas(db):
    for i in range(0,db,1):
        print(random.randint(1,9),end=" ")
    print()
veletlenszamkiiratas(5)

def szovegvisszafele(szoveg):
    for index in range(len(szoveg)-1,-1,-1):
        print(szoveg[index], end="")
    print()
szovegvisszafele("kalapács")

def szovegvisszafelefv(szoveg):
    visszaszoveg = ""
    for index in range(len(szoveg)-1,-1,-1):
        visszaszoveg += szoveg[index]
    return visszaszoveg
    

print(szovegvisszafelefv("kalapács"))

#irjon egy fv-t ami egy szórol eldönti hogy palindrom-e és vissza adja válaszul 
def palindromszoveg(palszoveg):
    # i = 0
    # while(i<len(palszoveg)//2 and palszoveg[i] == palszoveg[len(palszoveg)-1-i]):
    #     i+=1
    # if(i>len(palszoveg)//2):
    #     return "palindrom"
    # else:
    #     return "Nem palindrom"
    if (palszoveg == szovegvisszafelefv(palszoveg)):
        return True
    else:
        return False
print(palindromszoveg("cig"))