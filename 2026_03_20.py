
def fajbeolvasas():
    fajl = open("szeleromu.txt","r",encoding="utf-8")
    db = int(fajl.readline())
    print(db)
    t = []
    for i in range(db):
        sor = fajl.readline()
        sor2 = sor.strip().split(";")
        t.append((sor2[0],(sor2[1]),(sor2[2]),int(sor2[3]),int(sor2[4]),int(sor2[5])))
    fajl.close()
    return t
def megszamlalas(adatok):
    db = 0
    evSz =int(input("Adja meg hogy melyik évben szeretné nézni hogy mennyi szélerő"))
    for i in range(0,len(adatok),1):
        if(evSz == adatok[i][5]):
            db += adatok[i][3]
    return db
# hf:
def main():
    adatok =fajbeolvasas()
    print(adatok)
    print(megszamlalas(adatok))
main()