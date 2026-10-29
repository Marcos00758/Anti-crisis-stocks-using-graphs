alimentos = ["Batata", "Frango", "Pão de Queijo", "Brócolis", "Carne", "Peixe", 
             "Cenoura", "Linguiça", "Tofu", "Nuggets", "Pastel", "Bacon", 
             "Berinjela", "Mandioca", "Salsicha", "Pimentão", "Kibe", "Empada"]

tempos_minutos = (20, 25, 12, 10, 18, 15, 14, 30, 12, 10, 8, 15, 16, 22, 5, 10, 18, 14)

dicionario = {}

for alimento, tempo in zip(alimentos,tempos_minutos):
    if tempo >= 15:
        dicionario[alimento] = tempo

print(sorted(dicionario))