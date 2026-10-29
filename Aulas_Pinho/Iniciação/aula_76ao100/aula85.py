dicionario = {"c": 3, "a": 7, "b": 2}

ordenado = dict(sorted(dicionario.items(), key=lambda item: item[0]))
print(ordenado)

ordenado1 = dict(sorted(dicionario.items(), key=lambda item: item[1]))
print(ordenado1)

ordenado2 = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse = True))
print(ordenado2)