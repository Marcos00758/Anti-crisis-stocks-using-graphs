perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = 0
numero_perguntas = 0
acertos = 0

for pergunta in perguntas:
    numero_perguntas += 1
    for chave, valor in pergunta.items():
        if chave != "Resposta":
            print(chave, valor)
        else:
            resposta = input("Qual a resposta correta(digite apenas o valor)? ")
            
            if resposta == valor:
                acertos += 1
                print(f"Parabéns! Você acertou {acertos} de {numero_perguntas}")
            else:
                print(f"Você errou! {acertos} acertos de {numero_perguntas} ")

    print(" ")     


            