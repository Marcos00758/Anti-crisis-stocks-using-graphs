"""Jogo de adivinhação com dicas
- O programa escolhe um número aleatório entre 1 e 100.
- O usuário tenta adivinhar.
- Após cada tentativa, o programa diz se o número é maior ou menor."""

import random

numero_secreto = random.randint(1, 100)
print("Tente adivinhar o número escolhido de 1 a 100")
tentativa = 0

while True:
    numero_digitado = int(input("Digite um número: "))
    tentativa += 1
    if numero_digitado == numero_secreto:  
        print(f'Parabéns, você acertou o número {numero_secreto} em {tentativa} tentativas')
        break
    elif numero_digitado < numero_secreto:
        print(f"O número secreto é maior do que o número digitado")
        print(f"Essa é a sua {tentativa}° tentativa")
    else:
        print(f"O número secreto é menor que o número digitado")
        print(f"Essa é a sua {tentativa}° tentativa")
