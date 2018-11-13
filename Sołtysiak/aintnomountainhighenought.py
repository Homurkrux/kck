import os
print("elo")
imie=["Douglas","Tom","Jeff","Harry","Big"]
nazwisko=["Scott","Hardy","Mynameis","Belafonte","Lebowski"]

while True:
    os.system("cls")
    print("Witamy serdecznie na Leakbook tutaj mozesz wpisac wszystkie dane które chcesz żebysmy ukradli")
    print("Wpisz 'NIII' żeby wyświetlić imię po podaniu nazwiska")
    print("Wpisz 'virtue' żeby wyswietlić nazwisko po podaniu imienia")
    print("Wpisz 'omegalul'ażeby wyświetlic wszystkich znajomych")
    print("Wpisz 'kocham' żeby dodać nowego znajomego")
    print("Wpisz 'nienawidze' zeby usunąć znajomego")
    print("Wpisz 'Piotr Frączewski moim mistrzem'ażeby orzymać informacje na temat autora")
    print("Powiedź 'wrogu' i wyjdź")
    wybor=input()
    if wybor=="NIII":
        print("podaj nazwisko")
        naz=input()
        for i in range(len(nazwisko)):
            if naz==nazwisko[i]:
                print("Imie i nazwisko osoby której szukasz to ",imie[i],nazwisko[i])
    elif wybor=="virtue":
        print("podaj imie")
        im=input()
        for i in range(len(nazwisko)):
            if im==imie[i]:
                print("Imie i nazwisko osoby której szukasz to ",imie[i],nazwisko[i])
    elif wybor=="omegalul":
        for i in range(len(imie)):
            print(imie[i],nazwisko[i])
    elif wybor=="kocham":
        print("podaj imie")
        imie.append(input())
        print("podaj nazwisko")
        nazwisko.append(input())
    elif wybor=="nienawidze":
        print("podaj imie")
        imie.remove(input())
        print("podaj nazwisko")
        nazwisko.remove(input())
    elif wybor=="Piotr Frączewski moim mistrzem":
        print("Autor tej strony jest akutalnie niedostepny ale jestem pewien ze uważa ze na dworze jest za ciepło")
    elif wybor=="wrogu":
        break
    else:
        print("ojojoj to nie jest żadna opcja skarbku przepisz poprawnie ")
    input()
