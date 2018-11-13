lista=[4,5,2,8,10]
def sprawdzZerolubJeden(znak):
    if znak=="1" or znak==1:
        return True
    elif znak=="0" or znak==0:
        return True
    else:
        return False
def najwieksza(liczba1,liczba2,liczba3):
    if liczba1>liczba2 and liczba1>liczba3:
        return 1
    elif liczba2>liczba1 and liczba2>liczba3:
        return 2
    elif liczba3>liczba1 and liczba3>liczba2:
        return 3
def dysjunkcja(zmiennaP,zmiennaQ):
    if sprawdzZerolubJeden(zmiennaP) and sprawdzZerolubJeden(zmiennaQ):
        if zmiennaP==1 and zmiennaQ==1:
            return 0
        else:
            return 1
    else:
        return "hell no"
def srodkowy(lista):
    if len(lista)%2==0:
        return "nie ma srodkowego elementu"
    else:
        return lista[int(len(lista)/2)]
def sumaLiczb(poczatekZakresu,koniecZakresu):
    suma=0
    for i in range(poczatekZakresu,koniecZakresu+1):
        if i%2!=0:
            suma=suma+i
    return suma
znak=int(input("podaj znak"))
liczba1=int(input("podaj liczbe 1"))
liczba2=int(input("podaj liczbe 2"))
liczba3=int(input("podaj liczbe 3"))
zmiennaP=int(input("podaj zmiennaP"))
zmiennaQ=int(input("podaj zmiennaQ"))
poczatekZakresu=int(input("podaj poczatek zakresu"))
koniecZakresu=int(input("podaj koniec zakresu"))
print(sprawdzZerolubJeden(znak))
print(najwieksza(liczba1,liczba2,liczba3))
print(dysjunkcja(zmiennaP,zmiennaQ))
print(srodkowy(lista))
print(sumaLiczb(poczatekZakresu,koniecZakresu))
