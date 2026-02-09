import random


def kockadobasS():
    lista1 = []
    for i in range(0,7,1):
        lista1.append(random.randint(1,17))
    print(lista1)
    return lista1
def kockadobasf():
    lista2 = []
    for i in range(0,7,1):
        lista2.append(random.randint(1,17))
    print(lista2)
    return lista2
def listaOsszegS():
    osszeg = 0
    index = 0
    lista1 = [31,20,12,22,34,4,7]
    for i in range(0,len(lista1),1):
        osszeg += lista1[index]
        index += 1
    
    print(osszeg)
def listaOsszegf():
    osszeg2 = 0
    index = 0
    lista2 = [9,19,2,2,22,14,6]
    
    while len(lista2) > index:
        osszeg2 += lista2[index]
        index+=1
    print(osszeg2)
    return osszeg2
def minimum():
    mine =100
    minh =-1
    i = 0
    lista1= [31,20,12,22,34,4,7]
    while len(lista1)> i:
        if lista1[i] > mine:
            mine == lista1[i]
            minh+=1
            i += 1
        print(mine)
def main():
    kockadobasS()
    kockadobasf()
    listaOsszegS()
    listaOsszegf()
    minimum()

main()