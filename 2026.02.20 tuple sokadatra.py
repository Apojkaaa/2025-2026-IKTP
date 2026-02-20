

def listafeltoltes():
    db = int(input())
    t = []
    for i in range(db):
        sor = input()
        st = sor.split(' ')
        tuple =(st[0],int(st[1]),int(st[2]))
        t.append(tuple)
    return t
def Mazsaosszegzes(adatok):
    osszeg = 0
    for i in range(0,len(adatok)1):
        osszeg += adatok[i][1]
def Hanyarnagyobb(adatok,ar):
    db = 0
    for i in range(0,len(adatok),1):
        if adatok(adatok[i][2]> ar):
            db =+ 1
    return db
def main():
    adatok = listafeltoltes()
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    #irjon egy fugvenyt ami visszadja az osszetett szerkezethbol hogy hany mazsa gyumi van 
    osszeg =Mazsaosszegzes()
main()