import random
#keszitsen egy fuggvenyt ami egy darabaszámtol fugg es vissza ad egy feltoltott listat [-10,50] közötti számokkal

def listafeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(-10,50)
        lista.append(szam)
    return lista
print(listafeltolt(5))
# készítsen egy függvényt ami bármilyen lista elemszámait megvizsgálva visszadja hogy mennyi poz szám van

def pozitivDb(szamokLista):
    darab = 0
    for i in range(0,len(szamokLista),1):
        if (szamokLista[i]>1):
            darab +=1
    return darab

#irjon egy függvényt ami megadja a legnagyobb szám indexét
#irjon egy függvényt ami megadja a lista elemeinek az átlagát 
# irjon egy függvény ami bármilyen lista elemeire kiszámolja a pozitiv szamok atlagat