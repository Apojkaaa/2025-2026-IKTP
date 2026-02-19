import math
def prime(szam):
    a = 2
    while(a<math.sqrt(szam) and szam% a != 0):
        a+=1
    return a>math.sqrt(szam)
def lnko(szam1,szam2):
    kisebb = szam1
    if (szam1>szam2):
        kisebb = szam2
    while (kisebb >=1 and not (szam1% kisebb == 0 and szam2 % kisebb == 0)):
        kisebb -= 1
    return kisebb
def main():
    a = 52
    b = 26
    print(prime(a))
    print(lnko(a,b))
main()