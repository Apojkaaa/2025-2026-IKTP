#generáljn egy listában 13db olyan 4 jegyű véletlen számokat amik, 3,5,7-re végződnek
#hány darab 3-ra 5-re 7-re
import random

n = 13
lista = []
for i in range(0,n,1):
    szam2=random.randint(100,999)
    veletlen=random.randint(1,3)
    if (veletlen==1):
        lista.append(szam2*10+3)
    elif(veletlen==2):
        lista.append(szam2*10+5)
    elif(veletlen==3):
        lista.append(szam2*10+7)
print(lista)

haromra = 0
otre = 0
hetre = 0
for i in range(0,len(lista),1):
    if (lista[i] % 10 ==3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        otre += 1
    else:
        hetre += 1
print("háromra végződő:",haromra)
print("ötre végződő:",otre)
print("hétre végződő:",hetre)

#számtani átlag
#mértani átlag
#hány szám van átlag alatt
#30 db 13. 17-re végzédő számokkal. hány oszhótható 13-mal és 17-tel
#bekérsz egy hosszabb szöveget, hány darab felhasználó által megadott betű van
#bekérsz két szót megmondod hogy hány betű eltérés van