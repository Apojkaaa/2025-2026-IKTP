import math # a math-ban lévő függvényeket tudjuk használni 
import random

a = 2
gyoka = math.sqrt(a)
print("gyök(" + str(a) + ") = ",gyoka)

felkerekit = math.ceil(gyoka) #
print("felsoegeszrész", felkerekit)
lekerekit = math.floor(gyoka)
print("alsoegeszreszleg", lekerekit)
kerekites = round(gyoka,2)
print("kerekites 2 tizedes jegyre:",kerekites)
hatvanyozas1 = math.pow(gyoka, 2)
print("gyoka négyzete:", hatvanyozas1)
alap = 2
kitevo = 5
hatvanyozas2 = math.pow(alap,kitevo)
print(alap,"^",kitevo,"=",hatvanyozas2)

vszam1 = random.randint(2,10)

print(vszam1)