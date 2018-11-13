import os
import random
"""zawartosc="wabadabalubdub"
plik_tekstowy=open("test.txt","w")
plik_tekstowy.write(zawartosc)
plik_tekstowy.close()
zawartosc="wabadabalubdub"
plik_tekstowy=open("test.txt","r")
print(plik_tekstowy.read())
plik_tekstowy.close()"""
"""tekst=[]
linian=input()
for i in range(3):
    linia=input()
    tekst.append(linia+"\n")
plik_tekstowy=open(linian,"w")
plik_tekstowy.writelines(tekst)
plik_tekstowy.close()
plik_tekstowy=open(linian,"r")
print(plik_tekstowy.read())
plik_tekstowy.close()
zrodlo=open("test.txt").readlines()
cel=open("test.txt","w")
for s in zrodlo:
    cel.write(s.replace("os","yc"))
cel.close()
nowy_katalog="C:\\Users\\student\\Desktop\\Sołtysiak\\OmegaLUL"
if not os.path.exists(nowy_katalog):
    os.makedirs(nowy_katalog)"""
tekst=[]
for i in range(5):
    linia=str(round(random.random(),5))+" "+str(round(random.random(),5))
    tekst.append(linia+"\n")
plik_tekstowy=open("test.txt","w")
plik_tekstowy.writelines(tekst)
plik_tekstowy.close()
