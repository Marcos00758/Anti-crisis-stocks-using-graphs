nome = "EDUARDO"
nome2 = "eduardo"

lista = [nome, nome2]

for variavel in lista:
    if hasattr(variavel, 'upper'):
        print(getattr(variavel, 'upper')())

