import os
import random
class wrog:
    hp=0
    imie="Lawby"
    def __init__(self):
        self.hp=random.randint(5,10)
        print("Stoisz na przeciw",self.imie)
        print(self.hp)
    def dajimie(self):
        return self.imie
    def atak(self):
        return random.randint(0,2)
    def otrzymywanieobrazen(self,ilosc):
        self.hp=self.hp-ilosc
    def pokarzhp(self):
        return self.hp
class bohater:
    hp=0
    imie=""
    def __init__(self):
        self.hp=random.randint(10,15)
        self.imie=input("jak nazywasz sie przybyszu?")
    def dajimie(self):
        return self.imie
    def atak(self):
        return random.randint(0,2)
    def otrzymywanieobrazen(self,ilosc):
        self.hp=self.hp-ilosc
    def pokarzhp(self):
        return self.hp
    def potion(self):
        leczenie=random.randint(1,4)
        self.hp+=leczenie
        return leczenie
wrog=wrog()
bohater=bohater()
while wrog.pokarzhp()!=0 and bohater.pokarzhp()!=0:
    print(wrog.dajimie(),"hp:",wrog.pokarzhp())
    print(bohater.dajimie(),"hp:",bohater.pokarzhp())
    print("co robisz?(1.atak 2.potek)")
    opcja=int(input())
    if opcja==1:
        iloscb=bohater.atak()
        wrog.otrzymywanieobrazen(iloscb)
        print("zadałeś",iloscb,"obrazen")
    elif opcja==2:
        leczenie=bohater.potion()
        print("uleczyłes sie",leczenie,"obrazen")
    print("wrog atakuje")
    iloscw=wrog.atak()
    bohater.otrzymywanieobrazen(iloscw)
    print("otrzymałes",iloscw,"obrazen")
    input()
if wrog.pokarzhp()==0:
    print("BRAWO POKONAŁES PRZECIWNIKA")
