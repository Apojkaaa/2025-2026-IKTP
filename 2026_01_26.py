
#Jancsi és juliska elmennek gombát gyüjteni mindennap. 14 napig folyatmatosan gyujtik majd összevetik az adatokat
#szimulald a gyüjtést. kosár nagysága 2,9 közötti lebegőpontos azaz tört szám 2 tizedes jegy pontossággal mind2 adatot külön tárold 
#vane bármelyiknek 8,5 kg nál több gemba ha igen kinél
#van e olyan köztök aki 1.9 és 5.1 között gyüjtött
#max min átlag db(2.1-2,4)
def vaneketjegyulistaban(lista):
    i = 0
    while (i<len(lista) and (lista[i]>= 10 and lista[i]<=99)):
        i+=1
    vane = i <len(lista)
    return vane


def main():
    szamok = [2,5,6,3,7,11,9,1,2]
    #van-e kétjegyű szám a listába
    vaneketjegyu = vaneketjegyulistaban(szamok)
    print(vaneketjegyu)
    print(szamok)
main()