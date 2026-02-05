import random
def listafeltoltes():
    lista= []
    for i in range(17):
        valsz = random.randint(0,100)
        if (valsz >= 50):
            lista.append(random.randint(120,200))
        else:
            lista.append(random.randint(50,120))
    return lista
def listaAtlag(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    atlag = osszeg/len(lista)
    return atlag
def listaMaximuma(lista):
    maxe= lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]> maxe):
            maxe = lista [i]
    return maxe
def listaMinimuma(lista):
    mine= lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]< mine):
            mine = lista [i]
    return mine
def vaneMaxpontos(lista):
    index = 0
    n = 200
    while (index<len(lista) and lista[index] != 200):
        index +=1
    vane = index < len(lista)
    return vane
def listaTerjedelme(lista):
    maximum = listaMaximuma(lista)
    minimum = listaMinimuma(lista)
def dontobejutottakdb(lista):
    db = 0
    for i in range(0,len(lista),1):
        ponthatar = 140 
        if(lista [i] >= ponthatar):
            db += 1
    return db
def dontobejutottakdb(lista):
    i=0
    while(i<len(lista) and lista[i] != 50):
        i+=1
    vane =i<len(lista)
    if (vane):
        return i
    else:
        return -1
def main():
    pontok = listafeltoltes()
    print(pontok)
    #2. feladat
    atlag =listaAtlag(pontok)
    print("Átlag:", round(atlag,2))
    #3 feladat
    terjedelem = listaTerjedelme(pontok)
    print("terjedelem",terjedelem)
    #4. feladat
    vaneMaxpont = vaneMaxpontos(pontok)
    if(vaneMaxpont):
        print("Van max pontos")
    else:
        print("Nincs max pontos")
    # 5. feladat 
    darab =dontobejutottakdb(pontok)
    print(darab)
    #6 feladat
    index =ertek50index(pontok)
    if(index == -1):
        print("nincs 50 pontos dolgozat a versenyen")
    else:
        #print("A",str(index),"van az 50 pontos dolgozat")
        print(f"A", (index),"van az 50 pontos doga")
main()