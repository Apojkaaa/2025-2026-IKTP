def beolvasas():
    fajl = open("resztvevok.txt","r",encoding="UTF-8")
    elsoSor=fajl.readline().strip()
    sorok = fajl.readlines()
    t =[]
    for sor in sorok:
        sor=sor.strip().split(";")
        t.append((sor[0],sor[1],sor[2],int(sor[3]),sor[4]))
    fajl.close()
    return t,elsoSor
def megszamlalas(adatok,elsoSor):
    db = 0
    for i in range(len(adatok)):
        if(elsoSor[1] == adatok[i][4]):
            db += 1
    return db
def main():
    adatok = beolvasas()[0]
    print(adatok)
    elsoSor = beolvasas()[1]
    print(megszamlalas(adatok,elsoSor))
main()