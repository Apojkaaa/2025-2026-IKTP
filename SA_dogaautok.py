def fajlBeolvasas():
    f = open("adatok.txt","r",encoding="UTF-8")
    t = []
    sorok = f.readlines()
    for sor in sorok:
        st = sor.strip().split("\t")
        t.append((st[0],int(st[1]),int(st[2]),int(st[3])))
    f.close
    return t
def maxE(adatok):
    maxErtek = 0
    for i in range(len(adatok)):
        if(adatok[i][3] > maxErtek):
            maxErtek = adatok[i][3]
    return maxErtek
def maxi(adatok,maxErtek):
    maxindex = adatok[0][3]
    lista = []
    maxe = maxErtek
    for i in range(len(adatok)):
        if(adatok[i][3] > maxe):
            lista.append(adatok[i][0])
    return lista
def kereses(adatok,rendszam):
    i = 0
    lista = []
    while(i<len(adatok) and adatok[i][0] != rendszam):
        if(adatok[i][3] > 95):
            lista.append(adatok[i][1],adatok[i][2])
    return lista

def main():
    print(fajlBeolvasas())
    adatok = fajlBeolvasas()
    print(maxE(adatok))
    maxErtek =maxE(adatok)
    print(maxi(adatok,maxErtek))
    rendszam = input("Adja meg a keresni kivant auto rendszamat: ")
    print(kereses(adatok,rendszam))
main()