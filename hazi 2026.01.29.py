#Jancsi és juliska elmennek gombát gyüjteni mindennap. 14 napig folyatmatosan gyujtik majd összevetik az adatokat
#szimulald a gyüjtést. kosár nagysága 2,9 közötti lebegőpontos azaz tört szám 2 tizedes jegy pontossággal mind2 adatot külön tárold 
#vane bármelyiknek 8,5 kg nál több gemba ha igen kinél
#van e olyan köztök aki 1.9 és 5.1 között gyüjtött
#max min átlag db(2.1-2,4)
import random
def listafeltolt(n):
    lista = []
    for i in range(0,n,1):
        lista.append(random.randint(200,900)/100)
    return lista
def vaneSzamnalNagyobb(szam,lista):
    index = 0
    while(index <len(lista) and lista[index] <= szam):
        index += 1
    vane = index <len(lista)
    return vane
    #ha index <len lista akkor a vane erteke true
    #de ha kissebb akkor a avane erteke false

def vaneketszamkozott(a,b,lista):
    index = 0
    #while(index <len(lista) and not (lista[index]   szam)):
    while(index <len(lista) and not (lista[index] >= a and lista[index]<=b)):
        index += 1
    vane = index <len(lista)
    return vane
def main():
    jancsi = []
    juliska = []
    #print(listafeltolt(14))
    jancsi = listafeltolt(14)
    juliska = listafeltolt(14)
    print("juliska",juliska)
    print("jancsi", jancsi)
    vaneJuliska =vaneSzamnalNagyobb(8.5,juliska,)
    if(vaneJuliska):
        print("Van Juliskánál 8.5-nél nagyobb ")
    else:
        print("Nincs juliskánál 8.5-nél nagyobb")

    vaneJancsi =vaneSzamnalNagyobb(8.5,jancsi)
    if(vaneJancsi):
        print("Van Jancsinál 8.5-nél nagyobb ")
    else:
        print("Nincs Jancsinál 8.5-nél nagyobb")
    vaneJuliskaKozott = vaneketszamkozott(4.9,5.1, juliska)
    if(vaneJuliskaKozott):
        print("Juliskanak van 4.9 és 5.1 közötti ertéke")
    else:
        print("Nincs Juliskának")
    vaneJancsikaKozott = vaneketszamkozott(4.9,5.1, jancsi)
    if(vaneJancsikaKozott):
        print("Jancsinak van 4.9 és 5.1 közötti ertéke")
    else:
        print("Nincs Jancsinak")
main()