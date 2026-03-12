def fajbeolvasas():
    fajl = open("gyumolcsok.txt","r",encoding="utf-8")
    # osszeszadat = fajl.read()
    # print(osszeszadat)
    # sorok =fajl.readlines()
    # print(sorok)
    # sor = fajl.readline().strip()
    # print(sor)
    db = int(fajl.readline())
    print(db)
    t = []
    for i in range(db):
        sor = fajl.readline()
        sor2 = sor.strip().split(" ")
        t.append((sor2[0],int(sor2[1]),int(sor2[2])))
    return t
    fajl.close()
def main():
    t = fajbeolvasas()
    print(t)
main()