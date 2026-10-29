# lista com dicionários dentro
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
]

ordenados = sorted(produtos, key=lambda item: item['nome'])
ordenados_inverso = sorted(produtos, key=lambda item: item['nome'], reverse = True)
print(ordenados)
print(ordenados_inverso)

print()

# dicionário puro
meu_dict = {'c': 3, 'a': 1, 'b': 2}

ordenado = dict(sorted(meu_dict.items(), key=lambda item: item[0]))
print(ordenado)
