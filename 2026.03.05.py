

def bevolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),st[4]))
    return lista
def kereses(adatok,datum):
    i = 0
    while (i < len adatok and not())
        i += 1
    vane = i<len(adatok)
    if(vane):
        return i
    else:
        return -1
def main():
    adatok = bevolvasasa()
    print(adatok)
    datum = input("Adjon meg egy datumot")
    index = kereses(adatok,datum)
main()