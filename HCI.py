import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
def robieniemniejliczb(tablica):
    j=1
    dobrzeliczb=[]
    for j in range(len(tablica)):
        if tablica[j]!=tablica[j-1]:
            dobrzeliczb.append(tablica[j])
    return dobrzeliczb
dane = pd.read_csv(r"sub1trial11.csv", delimiter=',', engine='python')
baza=pd.DataFrame(dane)
sygnal=baza["sygnal"]
liczba=baza["liczba"]
t=np.linspace(0,38, 200*38)
sygnalprzef=ag.pasmowozaporowy(sygnal,200,49,51)
sygnalprzefiltrowany=ag.pasmowoprzepustowy(sygnalprzef,200,1,50)
plt.plot(t,sygnal)
plt.ylabel("Amplituda [-]")
plt.xlabel("Czas [s]")
plt.show()
plt.plot(t,sygnalprzef)
plt.ylabel("Amplituda [-]")
plt.xlabel("Czas [s]")
plt.show()
plt.plot(t,sygnalprzefiltrowany)
plt.ylabel("Amplituda [-]")
plt.xlabel("Czas [s]")
plt.show()
print(sygnal.mean())
print(sygnal.max())
print((0.9213993447036032+1.1333728720207226)/2)
duzoliczb=[]

for i in range(len(sygnal)):
    if sygnal[i]>1.027386108362163:
        duzoliczb.append(liczba[i])
print("Osoba badana wymrugała następujący ciąg liczb:",robieniemniejliczb(duzoliczb))
