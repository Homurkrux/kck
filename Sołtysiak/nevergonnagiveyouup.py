import os
import random
print("elo")
def tworzenie_folderu(nowy_katalog):
    sciezka="C:\\Users\\student\\Desktop\\Sołtysiak\\"
    if not os.path.exists(sciezka+nowy_katalog):
        os.makedirs(sciezka+nowy_katalog)
def tworzenie_plikow(ilosc):
    for i in range(ilosc):
        plik=open("kappapride\\"+str(i)+".txt","w")
        plik.write("i will never give you up")
        plik.close()
def kolumny_wiersze():
    plik=open("kolumnywiersze.txt","w")
    for i in range(3):
        linia=str(round(random.random(),3))+" "+str(round(random.random(),3))+" "+str(round(random.random(),3))+" "+str(round(random.random(),3))+" "+str(round(random.random(),3))+" "+str(round(random.random(),3))+" "+str(round(random.random(),3))
        plik.write(linia+"\n")
    plik.close()
def otwieranie_pliku(nazwapliku):
    plik=open(nazwapliku,"r")
    for linia in plik:
        print(linia)
    plik.close()

nowy_katalog=input()
tworzenie_folderu(nowy_katalog)
ilosc=int(input("ile plików od 10 do 30 stworzyć?"))
tworzenie_plikow(ilosc)
kolumny_wiersze()
nazwapliku=input("jaki plik otworzyc?")
otwieranie_pliku(nazwapliku)
