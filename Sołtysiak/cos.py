import random
import time
"""los= random.random()*2
zao=round(los,4)
print(zao)
print("%.4f" %zao)

import random
slo="konstantynopolitanczykkiewiczowna"
lok= random.choice(slo)
print(lok)

cyf=0
start=time.clock()
while cyf!=1:
    cyf=int(input("nie wcisnales '1'"))

koniec=time.clock()
czas=koniec-start
print(czas)

print("poczatek", time.ctime())
time.sleep(5)
print("koniec:".time.ctime())
print("watch out this place is bout to blow")
for i in range (5,0,-1):
        print(i)
        time.sleep(1)
print("KABOOOOOOOOOOOOOOM")
for i in range(1,7):
    print(random.randint(0,49))"""
kek=0
for i in range(0,5):
    cyf=0
    slo="abcdefghijklmnoprstuwxyz"
    lit=random.choice(slo)
    print(lit)
    start=time.clock()
    while cyf!=lit:
        cyf=input("nie wcisnales litery")

    koniec=time.clock()
    czas=koniec-start
    print(czas)
    kek+=czas
print(kek/5)
