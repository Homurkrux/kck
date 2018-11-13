"""print("elo")
def dzialanie(liczba1,liczba2):
    suma=liczba1+liczba2
    kwadrat=suma**2
    wynik= kwadrat-1
    return wynik
for i in range(3):
    pierwsza=int(input())
    druga=int(input())
    wynik=dzialanie(pierwsza,druga)
    print(wynik)"""

def rysuj(dlugosc=3,szerokosc=3,element=4):
    for i in range(dlugosc):
        for j in range(szerokosc):
            print(element,end='')
        print()
rysuj(2,3,'!@#$%^&*')
rysuj(3,4,'*')
rysuj()
def cos(gwiazdka):
    while gwiazdka>0:
        print("*")
        gwiazdka-=1

cos(5)
lista=[1,2,3,4,5,6,7,8,9]
def sumowanie(lista):
    if len(lista)>0:
        print(lista)
        return lista[0]+sumowanie(lista[1:])
    else:
        return 0

wynik=sumowanie(lista)
print(wynik)

def silnia(liczba):
    if liczba>0:
        return liczba*silnia(liczba-1)
    else:
        return 1
wynikk=silnia(5)
print(wynikk)
def dlugosc(lista):
    if len(lista)>0:

        return 1+dlugosc(lista[1:])
    else:
        return 0
cos=dlugosc(lista)
print(cos)

def ost(lista):
    if len(lista)>1:

        return ost(lista[1:])
    else:
        return lista[0]
kappa=ost(lista)
print(kappa)

def nty(lista,n):
    if len(lista)>n:
        return nty(lista[1:],n-1)
    else:
        return lista[0]
n=int(input())
zappa=nty(lista,n)
print(zappa)
