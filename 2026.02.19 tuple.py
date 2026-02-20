# a = 23
# b = "alma"
# c = True
# t = [a,b,c,["k1,k2"]]
# t[0]
#irj egy fuggvenyt ami megadja hogy melyik honapban volt a legjobb az ertek
def maxindex(lista):
    maxi=0
    for i in range(0,len(lista),1):
        if(lista[i]>lista[maxi]):
            maxi = i
    return maxi
# def jegyekMax(lista):
#     maxe = -1
#     for i in range(0,len(lista),1):
#         if lista[i]>maxe:
#             maxe = lista[i]
            # print(maxe)
def maxindex2(szamok,honapok):
    maxi = 0
    honap = honapok[0]
    for i in range(len(szamok)):
        if(szamok[i]>szamok[maxi]):
            maxi = i
            honap =honapok[i]
    return(honap,maxi, szamok[maxi])

def main():
    honapok =  ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
    jani = [4.0 , 3.8 , 4.2 , 4.1 , 3.8 , 4.2 , 3.0 , 3.6 , 4.2 , 3.0 , 4.6 , 4.2 ]
    #print(jegyekMax(jani))
    maxi = maxindex(jani)
    print(honapok[maxi])
    # tordeles - split
    szoveg = "Jani 2000 10 03 "
    print(szoveg)
    tordelt = szoveg.split(" ")
    adat = (tordelt[0], int(tordelt[1]),int(tordelt[2]),int(tordelt[3]))
    print(tordelt)
    print(2026-int(tordelt[1]))
    print(adat)
    szoveg2 ="2026.02.19 3 Programozás"
    tordelt2 = szoveg2.split(" ")
    adat2 = (tordelt2[0])
    print(adat2)
    datum = tordelt2[0].split(".")
    print(datum[1])
    szoveg3 ="IOV-878,Gados Peter,vz5551616v,2003.03.20"
    tordelt3 =szoveg3.split(",")
    adat3 = (tordelt[3])
    print(adat3[0])
    vezeteknev = tordelt3[1].split(" ")
    print(vezeteknev[0])
    # 5
    # alma 12 500
    # körte 10 600
    # szilva 13 300
    # cseresznye 8 1200
    # meggy 6 1150
    st ="ABC123 Kis Pista KJ-6746896859462 1992_03_10"
main()