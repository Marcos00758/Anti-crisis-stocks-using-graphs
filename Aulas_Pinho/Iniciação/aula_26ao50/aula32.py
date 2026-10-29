#pedir um número, informar se ele é par ou ímpar e se o usuário não
#digitar um número inteiro dizer que não é um número
numero = input("Digite um número inteiro: ")
try:
    numeroint = int(numero)
    if (numeroint % 2) == 0:
        print("O seu número é par.")
    else:
        print("O seu número é ímpar.")
except:
    print("Você não digitou um número inteiro")
    
# Perguntar a hora (apenas inteiro) e dizer
#Bom dia (0-11) boa tarde(12-17) boa noite (18-23)

hora = input("Qual o horário atual (0 a 24)? ")
try:
    horaint = int(hora)
    if horaint<12 or horaint == 24:
        print("Bom dia!")
    elif horaint<18 and horaint>11: #não é necessário botar o AND horaint<11
        print("Boa Tarde!")
    elif horaint <24:
        print("Boa Noite!")
    else:
        print("Você digitou uma hora maior do que 24.")
except: 
    print("Você digitou a hora incorretamente, tente novamente.")

#pedir o nome do usuário e falar se tiver até 4 letras é curto
# de 5 a 6 é normal e mais que 6 é muito grande
nome = input("Digite o seu 1° nome: ")

nomeqtd = len(nome)
if nomeqtd <=4:
    print(f"Seu nome {nome} é curto.")
elif nomeqtd <=6:
    print(f"Seu nome {nome} é normal.")
else:
     print(f"Seu nome {nome} é muito grande!")
