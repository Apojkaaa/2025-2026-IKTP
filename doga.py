import random 
a = random.randint(10.99)

for a in range(0,a,1):
    b = random.randint(100,999)
    print (b,end=" ")
szoveg= input("adjon meg egy szöveget ")
if(len(szoveg) % 2 ==0):
    index = len(szoveg[index])
    print(szoveg[index])
else:
    index1 =len(szoveg//2)
    index2 =len(szoveg//2) -1
    print(szoveg[index1], szoveg[index2])

for ix in range(0,len(szoveg),1):
    print(szoveg[ix],end="$")