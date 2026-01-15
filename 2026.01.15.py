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