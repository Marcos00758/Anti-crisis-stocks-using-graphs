coletas = (
    ("Cobre", "Metal"), ("Enxofre", "Químico"), ("Ferro", "Metal"), 
    ("Carvão", "Químico"), ("Calcário", "Mineral"), ("Ouro", "Metal"), 
    ("Salitre", "Químico"), ("Prata", "Metal"), ("Quartzo", "Mineral"),
    ("Chumbo", "Metal"), ("Ácido Sulfúrico", "Químico"), ("Argila", "Mineral"),
    ("Estanho", "Metal"), ("Mica", "Mineral"), ("Fósforo", "Químico"),
    ("Tungstênio", "Metal"), ("Granito", "Mineral"), ("Etanol", "Químico")
)

# Objetivo: Inverter a relação dos dados. Criar um dicionário onde a chave é a Categoria 
# (ex: 'Metal') e o valor é uma Lista contendo todos os materiais que pertencem a ela

dicionario = {}

for itens in coletas:
    lista = []
    for i in range(len(coletas)):
        if coletas[i][1] == itens[1]:
            lista.append(coletas[i][0])
    dicionario[itens[1]] = lista



print(dicionario)