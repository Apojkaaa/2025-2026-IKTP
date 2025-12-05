"""
lista - dinamikus 
-tudunk bele uj elemet rakni ezzel nő az elemszám
tudunk berlole tötölni ezzle csökken az elemszam
- lekérhető bármelyik eleme 
deklarálás: + inicializálás
létrehozás + kezdőérték adás:
lista_neve= []
új elem hozzaadása
lista_neve.append (ujelem)
elem törlése 
lista_neve.remove(elem)
beégett lista 
lista_neve = [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""
Elso_lista = [3,2,5,7,1]
print(Elso_lista)
print("Első elem: ", Elso_lista[0])
print("lista hossza:", len(Elso_lista))
print("utolsó elem", Elso_lista[-1])
# házi feladat: számok átlaga (13 elemn) háy db páros szám van e benne 0
szoveg = "alma"
dúpe = "ny"
print(szoveg)
if "sz" in szoveg:
    print("van benne sz betű")
else:
    print("nincs benne sz betű")

index = 0
while(index<len(szoveg)-1 and  not (szoveg[index] == dube[0] and szoveg[index+1] == dube [2])):
    index+=1
if(index<len(szoveg)-1):
    print("van benne")
else:
    print("nincsen benne")


palindrom-e
ujszoveg = ""
for index in range(len(szoveg) -1,-1,-1):
    ujszoveg+= szoveg[index]
if(ujszoveg == szoveg):
    print("A szöveg palindrom")
else:
    print("A szöveg nem palindrom")

j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-1-j]):
    j+=1
if (j<len(szoveg)/2):
    print("A szoveg nem palindrom")
else:
    print("A szoveg palindrom")