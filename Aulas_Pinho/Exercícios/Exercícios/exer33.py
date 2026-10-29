notas_brutas = (("Ana", 8.5), ("Bruno", 5.0), ("Carlos", 9.2), ("Diana", 4.5), ("Eduardo", 7.0), ("Fernanda", 9.8))

aprovados = []
reprovados = []

dicionario = {}

for item in notas_brutas:
    if item[1] >= 7:
        aprovados.append(item[1])
    else:
        reprovados.append(item[1])

dicionario = {'Aprovados': aprovados, 'Reprovados': reprovados}

print(dicionario)