nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade: #podia ser só if nome and idade: (pega os casos que ambos aparecem)
    print("Você deixou campos vazios")

else:   
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print("Seu nome tem espaços")
    else: 
        print("Seu nome não tem espaços")

    qtd = len(nome)
    print(f"Seu nome tem {qtd} letras")

    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")

