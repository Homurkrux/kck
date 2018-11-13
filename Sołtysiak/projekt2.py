import os
import random

while True:
    os.system("cls")
    print("Witaj w moim programie przybyszu")
    print("Zeby otrzymac informacje o autorze wcisnij e")
    print("Zeby zagrac w gre wcisnij w")
    print("Zeby wyjsc wcisnij q")
    op=input()
    if op=="e":
        print("Witam serdecznie jestem Wiktor i bardzo ciesze sie ze zdecydowałes skorzystac z mojego programu")
    elif op=="w":
        los=random.randint(0,99)
        print("Zgadnij liczbe w zakresie od 0 do 99")

        for i in range(0,7):
            gu=int(input())
            if gu>los:
                print("za duzo")

            elif gu<los:
                print("za mało")

            elif gu==los:
                print("wygrałes")
                break
            if i==6:
                print("przegrałeś")
                break

    elif op=="q":
        break
    else:
        print("nie podales istniejacej opcji")
    input()
