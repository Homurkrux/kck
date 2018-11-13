import random
piedziesiatt=1
telefon=1
publicznoscc=1
hajs=0
def hajs(hajs):
    return hajs+1
def losowaniePytania():
        numer=random.randint(0,5)
        if numer==1:
            return 1
        elif numer==2:
            return 2
        elif numer==3:
            return 3
        elif numer==4:
            return 4
        elif numer==5:
            return 5

def piedziesiat(piedziesiatt):
    if piedziesiat==0:
        return "nie masz juz tego koła ratunkowego"
    else:
        return "odpowiedz poprawna to odp A albo odp B"
def przyjaciel(przyjaciel):
    if przyjaciel==0:
        return "nie masz juz tego koła"
    else:
        odpowiedz=random.randint(0,4)
        if odpowiedz==1:
            return "Przyjaciel mówi ze poprawna odpowiedz to A"
        elif odpowiedz==2:
            return "Przyjaciel mówi ze poprawna odpowiedz to B"
        elif odpowiedz==3:
            return "Przyjaciel mówi ze poprawna odpowiedz to C"
        elif odpowiedz==4:
            return "Przyjaciel mówi ze poprawna odpowiedz to D"
def publicznosc(publicznoscc):
    if przyjaciel==0:
        return "nie masz juz tego koła"
    else:
        odpowiedz=random.randint(0,4)
        if odpowiedz==1:
            return "Publicznosc mówi ze poprawna odpowiedz to A"
        elif odpowiedz==2:
            return "Publicznosc mówi ze poprawna odpowiedz to B"
        elif odpowiedz==3:
            return "Publicznosc mówi ze poprawna odpowiedz to C"
        elif odpowiedz==4:
            return "Publicznosc mówi ze poprawna odpowiedz to D"


def pytanie1(piedziesiatt,telfon,publicznoscc):
    print("tresc pytania1,chcesz urzyc kola ratunkowego?")
    print("A B C D")
    wyborkoloratunkowe=input("Tak/Nie?")
    if wyborkoloratunkowe=="Tak":
        print("które?")
        print("50na50/telefon do przyjaciela/pomoc publiczności")
        koloratunkowe=input()
        if koloratunkowe=="50na50":
            print(piedziesiat(piedziesiatt))
            global piedziesiatt
            piedziesiatt=0
        if koloratunkowe=="telefon do przyjaciela":
            print(przyjaciel(telefon))
            global przyjaciel
            przyjaciel=0
        if koloratunkowe=="pomoc publiczności":
            print(publicznosc(publicznoscc))
            global publicznoscc
            publicznoscc=0
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
    elif wyborkoloratunkowe=="Nie":
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
def pytanie2(piedziesiatt,telfon,publicznoscc):
    print("tresc pytania2,chcesz urzyc kola ratunkowego?")
    print("A B C D")
    wyborkoloratunkowe=input("Tak/Nie?")
    if wyborkoloratunkowe=="Tak":
        print("które?")
        print("50na50/telefon do przyjaciela/pomoc publiczności")
        koloratunkowe=input()
        if koloratunkowe=="50na50":
            print(piedziesiat(piedziesiatt))
            global piedziesiatt
            piedziesiatt=0
        if koloratunkowe=="telefon do przyjaciela":
            print(przyjaciel(telefon))
            global przyjaciel
            przyjaciel=0
        if koloratunkowe=="pomoc publiczności":
            print(publicznosc(publicznoscc))
            global publicznoscc
            publicznoscc=0
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
    elif wyborkoloratunkowe=="Nie":
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
def pytanie3(piedziesiatt,telfon,publicznoscc):
    print("tresc pytania3,chcesz urzyc kola ratunkowego?")
    print("A B C D")
    wyborkoloratunkowe=input("Tak/Nie?")
    if wyborkoloratunkowe=="Tak":
        print("które?")
        print("50na50/telefon do przyjaciela/pomoc publiczności")
        koloratunkowe=input()
        if koloratunkowe=="50na50":
            print(piedziesiat(piedziesiatt))
            global piedziesiatt
            piedziesiatt=0
        if koloratunkowe=="telefon do przyjaciela":
            print(przyjaciel(telefon))
            global przyjaciel
            przyjaciel=0
        if koloratunkowe=="pomoc publiczności":
            print(publicznosc(publicznoscc))
            global publicznoscc
            publicznoscc=0
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
    elif wyborkoloratunkowe=="Nie":
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
def pytanie4(piedziesiatt,telfon,publicznoscc):
    print("tresc pytania4,chcesz urzyc kola ratunkowego?")
    print("A B C D")
    wyborkoloratunkowe=input("Tak/Nie?")
    if wyborkoloratunkowe=="Tak":
        print("które?")
        print("50na50/telefon do przyjaciela/pomoc publiczności")
        koloratunkowe=input()
        if koloratunkowe=="50na50":
            print(piedziesiat(piedziesiatt))
            global piedziesiatt
            piedziesiatt=0
        if koloratunkowe=="telefon do przyjaciela":
            print(przyjaciel(telefon))
            global przyjaciel
            przyjaciel=0
        if koloratunkowe=="pomoc publiczności":
            print(publicznosc(publicznoscc))
            global publicznoscc
            publicznoscc=0
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
    elif wyborkoloratunkowe=="Nie":
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
def pytanie5(piedziesiatt,telfon,publicznoscc):
    print("tresc pytania5,chcesz urzyc kola ratunkowego?")
    print("A B C D")
    wyborkoloratunkowe=input("Tak/Nie?")
    if wyborkoloratunkowe=="Tak":
        print("które?")
        print("50na50/telefon do przyjaciela/pomoc publiczności")
        koloratunkowe=input()
        if koloratunkowe=="50na50":
            print(piedziesiat(piedziesiatt))
            global piedziesiatt
            piedziesiatt=0
        if koloratunkowe=="telefon do przyjaciela":
            print(przyjaciel(telefon))
            global przyjaciel
            przyjaciel=0
        if koloratunkowe=="pomoc publiczności":
            print(publicznosc(publicznoscc))
            global publicznoscc
            publicznoscc=0
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0
    elif wyborkoloratunkowe=="Nie":
        print("Jaka jest twoja odpowiedz?")
        odpowiedz=input()
        if odpowiedz=="A":
            print("Tak to jest poprawana odpowiedz")
            return 1
        else:
            print("To nie jezt poprawna odpowiedz")
            return 0

for i in range(5):
    pytanie= losowaniePytania()
    if pytanie==1:
        poprawnosc=pytanie1(piedziesiatt,telefon,publicznoscc)
        if poprawnosc==1:
            hajs+=1
        else:
            break
    elif pytanie==2:
        poprawnosc=pytanie2(piedziesiatt,telefon,publicznoscc)
        if poprawnosc==1:
            hajs+=1
        else:
            break
    elif pytanie==3:
        poprawnosc=pytanie3(piedziesiatt,telefon,publicznoscc)
        if poprawnosc==1:
            hajs+=1
        else:
            break
    elif pytanie==4:
        poprawnosc=pytanie4(piedziesiatt,telefon,publicznoscc)
        if poprawnosc==1:
            hajs+=1
        else:
            break
    elif pytanie==5:
        poprawnosc=pytanie5(piedziesiatt,telefon,publicznoscc)
        if poprawnosc==1:
            hajs+=1
    else:
        break
print("Wygrałeś",hajs,"milionów")
