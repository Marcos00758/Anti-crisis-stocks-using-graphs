atletas = ("James", "Julie", "Mikey", "Sarah")
tempos_esteira = (12.5, 11.8, 14.2, 13.1)

dicionario = {}
i = 1

for atleta, tempo in zip (atletas, tempos_esteira):
    print(f'Treino {i}: A {atleta} em {tempo:.2f} minutos!')
    i += 1


