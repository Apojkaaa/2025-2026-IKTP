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
main()