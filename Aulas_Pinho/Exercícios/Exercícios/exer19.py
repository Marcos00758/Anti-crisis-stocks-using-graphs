numeros = [1, 3, 5, 2, 4]
numeros.sort()
print(numeros)

lista = []
pares = []
impares = []

for numero in numeros:
    if (numero % 2) == 0:
        pares.append(numero)
    else:
        impares.append(numero)

lista = [pares] + [impares]
print(lista)