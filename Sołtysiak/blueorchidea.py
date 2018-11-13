import os

szyfr={'a': 'f', 'b': 'c', 'c': 'p', 'd': 's', 'e': 'w', 'f': 'i', 'g': 'a',
       'h': 't', 'i': 'r', 'j': 'e', 'k': 'z', 'l': 'o', 'm': 'n', 'n': 'y',
       'o': 'g', 'p': 'k', 'r': 'l', 's': 'd', 't': 'b', 'u': 'j', 'w': 'm',
       'y': 'h', 'z': 'u'}

listaLiter=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r',
            's','t','u','w','y','z')

samogloski=('a','e','i','o','u','y')
slo=[]
krot=[]
while True:
    os.system("cls")
    print("w info")
    print("e zad jeden")
    print("r zad dwa")
    print("q przerwac")
    opc=input()
    if opc=="q":
        break
    elif opc=="w":
        print("Boy i know you blue")
    elif opc=="e":
        print("jak długie słowo?")
        dl=int(input())
        print("podawaj litery i co kazda pacnij enter")
        for i in range(0,dl):
            cos=input()
            slo.append(szyfr[cos])
        print(slo)
    elif opc=="r":
        print("jak dlugie slowo?")
        dlu=int(input())
        print("podawaj litery i co kazda pacnij enter")
        for i in range(dlu):
            xd=input()
            for j in range(len(listaLiter)):
                if xd==listaLiter[j]:
                    if (xd in samogloski ):
                        krot.append(listaLiter[j-1])
                    else:
                        krot.append(listaLiter[j+1])
        print(krot)

    input()
#samogloski w lewo spolgloska w prawo
