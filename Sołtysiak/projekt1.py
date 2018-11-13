import os

while True:
    os.system("cls")
    print("Witam w menu mojego programu prosze wybrac jedna z obcji ażeby uruchomić daną funkcje")
    print("a- informacja o autorze")
    print("b- program wyswietlający liczby podzielne przez 2 ale nie przez 5 z zakresu od 0 do 150")
    print("c- program wyswietlający liczby podzielne przez 4 z zakresu od -50 do 0")
    print("d- program wyliczający sumę wszystkich liczb od 0 do 100")
    print("q- wyłączenie programu")
    op=input()
    if op=="q":
        break
    elif op=="a":
        print("Dziękuje za skorzystanie z mojego projektu!\n !!!MIŁEGO DNIA!!!")
    elif op=="b":
        for i in range(0,151):
            if i%2==0 and i%5!=0:
                print(i)
    elif op=="c":
        k=-50
        while k<0:
            if k%4==0:
                print(k)
            k=k+1
    elif op=="d":
        cos=0
        for i in range(0,101):
            cos=cos+i
            if i==100:
                print(cos)

    input()
