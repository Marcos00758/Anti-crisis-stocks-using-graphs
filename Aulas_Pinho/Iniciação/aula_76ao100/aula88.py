produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

lista = []

for produto in produtos:
    if produto['preco'] > 10:
        lista.append(produto)


for item in lista:
    print(f"nome: {item['nome']}, preco: {item['preco']}")
