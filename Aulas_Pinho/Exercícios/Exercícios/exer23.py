itens_coletados = ["graveto", "pedra", "graveto", "batata", "pedra", "graveto", "espada"]

dicionario = {}

for item in itens_coletados:
    if item in dicionario:
        continue
    else:
        dicionario[item] = itens_coletados.count(item)
        
print(dicionario)