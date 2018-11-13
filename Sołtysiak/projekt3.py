import time
import os
import random
while True:
    os.system("cls")
    l1=random.randint(0,9)
    l2=random.randint(0,9)
    print("wykonaj",l1,"+",l2,"=?")
    start1=time.clock()
    wyn1=int(input())
    while wyn1!=l1+l2:
        print("to nie jest prawidłowy wynik")
        break
    stop2=time.clock()
    czas1=round(stop2-start1,3)
    input()

    l3=random.randint(0,9)
    l4=random.randint(0,9)
    print("wykonaj",l3,"+",l4,"=?")
    start3=time.clock()
    wyn2=int(input())
    while wyn2!=l3+l4:
        print("to nie jest prawidłowy wynik")
        break
    stop4=time.clock()
    czas2=round(stop4-start3,3)
    input()

    l5=random.randint(0,9)
    l6=random.randint(0,9)
    print("wykonaj",l5,"+",l6,"=?")
    start5=time.clock()
    wyn3=int(input())
    while wyn3!=l5+l6:
        print("to nie jest prawidłowy wynik")
        break
    stop6=time.clock()
    czas3=round(stop6-start5,3)
    input()

    l7=random.randint(0,9)
    l8=random.randint(0,9)
    print("wykonaj",l7,"+",l8,"=?")
    start7=time.clock()
    wyn4=int(input())
    while wyn4!=l7+l8:
        print("to nie jest prawidłowy wynik")
        break
    stop8=time.clock()
    czas4=round(stop8-start7,3)
    input()

    l9=random.randint(0,9)
    l10=random.randint(0,9)
    print("wykonaj",l9,"+",l10,"=?")
    start9=time.clock()
    wyn5=int(input())
    while wyn5!=l9+l10:
        print("to nie jest prawidłowy wynik")
        break
    stop10=time.clock()
    czas5=round(stop10-start9,3)
    input()
    print(czas1)
    print(czas2)
    print(czas3)
    print(czas4)
    print(czas5)
    print("sredni czas prób",round((czas1+czas2+czas3+czas4+czas5)/5,3))
    input()
