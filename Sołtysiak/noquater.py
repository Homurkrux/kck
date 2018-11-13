cos=[2,3,4,5,1,5,3,2,23,5,23,235,532,235,21,666,242,5235,63462134,234235,2,235,2342,53]
def ogarniamtablice(cos):
    ostatni=cos[-1]
    return ostatni
def ogon(cos):
    x=cos[1:]
    return x
def maksimum(cos):
    x=cos[0]
    for i in range(len(cos)):
        if x<cos[i]:
            x=cos[i]
    return x
def minimum(cos):
    x=cos[0]
    for i in range(len(cos)):
        if x>cos[i]:
            x=cos[i]
    return x
def dlugosc(cos):
    x=0
    for i in cos:
        x+=1
    return x
def nty(liczba1):
    return cos[liczba1-1]
def alternatywa(pierwsza,druga):
    if pierwsza==0 and druga==1:
        return 1
    elif pierwsza==0 and druga==0:
        return 0
    elif pierwsza==1 and druga==0:
        return 1
    elif pierwsza==1 and druga==1:
        return 1
    else:
        print("mozesz wpisac tylko 0 albo 1 ")
def dodawanie(liczba1,liczba2):
    suma=liczba1+liczba2
    return suma
def mnozenie(liczba1,liczba2):
    iloczyn= liczba1*liczba2
    return iloczyn
def odejmowanie(liczba1,liczba2):
    roznica= liczba1-liczba2
    return roznica
liczba1=int(input("podaj l1"))
liczba2=int(input("podaj l2"))
pierwsza=int(input("podaj p"))
druga=int(input("podaj d"))
print(dodawanie(liczba1,liczba2))
print(mnozenie(liczba1,liczba2))
print(odejmowanie(liczba1,liczba2))
print(ogarniamtablice(cos))
print(ogon(cos))
print(maksimum(cos))
print(minimum(cos))
print(dlugosc(cos))
print(len(cos))
print(nty(liczba1))
print(alternatywa(pierwsza,druga))
