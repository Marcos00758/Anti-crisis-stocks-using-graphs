condicao = True

while condicao:
    nome = input("Digite seu nome: ")
    if nome != "sair":
        print(f"Seu nome é {nome}") #Como a condição nãsao muda, isso é um looping
    if nome == "sair":
        break

print("Inalcançável, nunca vai acontecer, porque antes é um"
"lopping infinito, só se cair no break")
