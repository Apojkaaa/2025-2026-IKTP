def fajbeolvasas():
    fajl = open("forgalom.txt","r",encoding="utf-8")
    elsoSor = fajl.readline()
    sorok = fajl.readlines()
    t = []
    for sor in sorok:
        sor = sor.strip().split(" ")
        t.append((int(sor[0]),int(sor[1]),int(sor[2]),int(sor[3]),sor[4]))
    fajl.close()
    return t ,elsoSor
def main():
    adatok = fajbeolvasas()
    print(adatok)
    t = adatok[0]
    elsoSor = adatok[1]
main()