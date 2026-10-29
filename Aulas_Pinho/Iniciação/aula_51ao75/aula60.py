lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista4 =[lista1] + [lista2] + [lista3]
print(lista4)
print(lista4[1][2])
print( )
for lista in lista4:
    for numero in lista:
        print(numero)

vazio = ""
for listass in lista4:
    for numeros in listass:
        vazio += str(numeros)

print(int(vazio))
        