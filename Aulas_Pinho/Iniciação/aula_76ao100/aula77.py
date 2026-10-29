lista = [1,2,3,4,5,6]
print(len(lista))

dicionario = {"nome":"eduardo", "sexo":"masculino"}
print(len(dicionario))

print(list(dicionario.items()))

for parametro, valor in dicionario.items():
    print(parametro,"=", valor)