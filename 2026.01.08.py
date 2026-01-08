import random
import math
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
matlag = math.pow(szorzat,1/n)
dba = 0
for index in range(0,n,1):
    if(atlag>lista[index]):
        dba += 1
print("számtani átlag alatti értékek elemszáma:",dba)
mossz = 0
for a in lista:
    if(matlag > a):
        mossz += a 
print("mértani átlag összege: ",mossz)
szoveg= "bekérsze gy hosszabb szöveget, hány darab felhasználó által megadott betű van benne?"
print(szoveg)
betu = input("adjon meg egy betűt: ")

dbbetu = 0
for karakter in szoveg:
    if (karakter ==betu):
        dbbetu += 1
print(dbbetu)

szo1 ="alma"
szo2 = "alkat"
kulonbseg = 0
minimumhossz = 0
if(len(szo1)>len(szo2)):
    minimumhossz = len(szo2)
else:
    minimumhossz = len(szo1)
for i in range(0,minimumhossz,1):
    if(szo1[i] != szo2[i]):
        kulonbseg += 1
print(kulonbseg)