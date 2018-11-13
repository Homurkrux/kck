"""sklep={"ser":3,"kawa":10,"szynka":5,"batonik":1,"cola":6,"wafle":7,"torebka":1000}
koszyk={}
print(sklep)
suma=0
print("wybierz rzeczy które chcesz kupic")

while True:
    opc=input()
    if opc=="koniec":
        break
    else:
        koszyk[opc]=sklep[opc]
        suma=suma+sklep[opc]
print("suma pieniedzy za twoje zakupy to :",suma)
print("twój koszyk to", koszyk)"""
"""import random
import os
ang={1:"dude",2:"duck",3:"big",4:"bannana"}
pol={1:"typek",2:"kaczka",3:"duzy",4:"banan"}
while True:
    os.system("cls")
    licz=random.randint(1,4)
    slowo=pol[licz]
    print(slowo)
    odp=input()
    if odp==ang[licz]:
        print("Dobrze")
    elif odp=="skoncz":
        break
    else:
        print("To nie jest dobra odpowiedź")
    print("wcisnij enter zeby cwiczyc dalej")
    input()"""
cos={}
while True:
    cos1=input()
    cos2=input()
    if cos2=="q":
        break

    cos[cos1]=cos2
print(cos)
