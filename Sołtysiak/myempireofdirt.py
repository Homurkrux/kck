import random
cos=0
max=0
min=10000
suma=0
cash=["Kasia","Zosia","Asia","Basia"]
johnny=[643,89463,654321,5412]
hurt=[]
"""for i in range(0,10):
    cash.append(random.random())"""
"""for i in range(len(cash)):
    if cash[i]==7:
        cos+=1
###print(cash)
print(cos)"""
"""for i in range(len(cash)):
    suma+=cash[i]
    if max<cash[i]:
        max=cash[i]
    if min>cash[i]:
        min=cash[i]
for i in range(99,-1,-1):
    johnny.append(cash[i])

print(cash)
print(johnny)
print(max)
print(min)
print(suma)
print(suma/len(cash))"""
"""print("+---+------+")
for i in range(len(cash)):
        print ("I",i,"I","%.2f" %cash[i],"I")

print("+---+------+")"""

hurt=johnny[:]
hurt.sort()
for i in range(len(hurt)):
    for j in range(len(johnny)):
        if hurt[i]==johnny[j]:
            print(cash[j],johnny[j])
