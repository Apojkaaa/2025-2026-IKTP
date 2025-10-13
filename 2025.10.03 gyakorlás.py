# generálj ki egy véletlen számot -10 és 10 között
# írasd ki a adott számot
import random
import math

a = random.randint (-5,5)*2
print("szám:"+ str(a))
# vegyyük aa szám abszolút 
# ha a szám negatív akkor szám*-1 különben önmaga
if a<0 :
    print("abs: "+ str (a*(-1)))
else:
    print("abs:" + str (a))
    # irassa ki a szám gyökét
    gyoka = math.sqrt(a)
    print("gyök(" + str(a) + ") = ",gyoka)
if (a>=0 ):
    print ("gyök(a):" +str (math.sqrt(a))) 
else:
    print("A negatív számnak nincs gyöke.")
if (a>0):
    print ("Pozitív")
else:
    if(a==0):
        print("nulla")
    else:
        print("Negatív")

#felhasználótól bekérés 
szoveg = input ("Adjon meg egy számot: ")
print(szoveg)

# HF Pdf 8-13
# szekvencia - utasítások sorozata
# szelekció - elágazás 
# Iterácioó - ciklus, ismétlés


# HF megoldás

sec = 3923
# 1 óra 5 perc 23 másodperc
#3600 + 300 + 23
ora = sec // 3600   
perc = (sec - ora * 3600) // 60
#mp =
print (ora,"óra")
print (perc,"perc")