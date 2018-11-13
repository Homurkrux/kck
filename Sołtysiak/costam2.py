import os
from colorama import init
from termcolor import colored
init()
"""for i in range(101,0,-5):
    print(i)
cyfra=0
while cyfra!=10:
    print(cyfra)
    cyfra+=1"""


while True:
    os.system("cls")
    print("aby zakonczyc program wcisnij q")
    print("wcisnij 2 zeby wyswietlic zadanie 2 ")
    print("wcisnij 3 zeby wyswietlic zadanie 3")
    print("wcisnij 4 zeby wyswietlic zadanie 4")
    znak = input()
    if znak == '2':
        for i in range(0,51):
            suma=0
            suma=suma+i
            if suma==50:
                print(suma)
    elif znak=='3':
        for i in range(0,101):
            if i==4:
                i+=1
            elif i==34:
                i+=1
            elif  57<=i<=74:
                i+=1
            elif  78<=i<=90:
                i+=1
            elif i==92:
                i+=1
            else:
                print(i)
    elif znak=='4':
        print("podaj wysokośc choinki")
        choi=int(input())
        for i in range(1,choi):
            for j in range(1)


    elif znak== 'q':
        break
    else:
        print("nie znam cie")
    input()
