import random
n = 30
lista =[]
for i in range (0,n,1):
    valtozo = random.randint(10,99)
    veletlen = random.randint(1,2)
    if(veletlen == 1):
        lista.append(valtozo*100+17)
    else:
        lista.append(valtozo*100+13)
print(lista)

osszeg = 0
for index in lista:
    osszeg += index
atlag = osszeg/n
print(round(atlag,2))

szorzat = 1
for elem in lista:
    szorzat *=elem
matlag = n.gyök(szorzat)