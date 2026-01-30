import random
def  szamBekeres():
    szam = int(input("Adjon meg egy számot 10,20 között: "))
    while szam < 10 or szam > 20:
        szam = int(input("Adjon meg egy számot ami 10 és 20 között van: "))
    return szam

def listaFv(n):
    lista = []
    for i in range(0,n,1):
        szam = random.randint(10,99)
        if(szam % 4 == 0):
            szam += 1
        lista.append(szam)
    return lista

def kereses(lista):
    while(i<len(lista) and lista [] % 10 != 7):
        i+=1
    vane = i <len(lista)
    if vane: return i
    else: return -1
def main():
    db=szamBekeres()
    print(db)
    print(listaFv(db))
    index =kereses(listaFv)
    if(index == -1):
        print("nincs a listában 7-tel osztható elem")
    else:
        print("Van a listában 7-tel osztható elem az",index+1,"helyen")
main()

#hf csinalj egy olyan lustat ami feltolti a francia kartyakkal és irni kell egy függvényt egy listával ami visszatér
#irjon egy függvényt ami megkeveri a paklit véletlen hely kivalasztásval
#irjon egy paraméteres függvényt ami megadja hogy hanyadik helyen szereple a megadott lapo
#kérjen be a falhsználotol egy lap értéket és adja meg hogy hanyadik helyen van