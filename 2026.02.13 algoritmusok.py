#irjon függvényt ami függ egy egész számtól és megadja, hogy prim vagy nem prim!
#irjon egy függvényt, ami megmodnja két pozitiv egész számról a LNKO-t

def prime(szam):
    for i in range(2,szam,1):
        if szam % i == 0:
            return ("Nem Prím")
        return("Prím")
def lnko(szam1,szam2):
    

def main():
    a = 13
    b = 26
    print(prime(a))
main()