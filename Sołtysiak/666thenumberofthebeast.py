"""cyfratrzy = ["III","3","trzy","three","..."]
while True:

    for i in range(len(cyfratrzy)):
        print(cyfratrzy[i])
    print(cyfratrzy[1:2])
    print(len(cyfratrzy))
    cyfratrzy[0]=input()
    print(cyfratrzy[0])
    cyfratrzy.append(input())
    input()"""
lista=[1,2,3]
print('ile elementów ma miec lista')
lista.remove(int(imput()))
cos=int(input())
n=cos-len(lista)
for i in range(n):
    print("podaj element")
    lista.append(int(input()))
for i in range(len(lista)):
    print(lista[i])
