#fazer uma lista de compras, onde o usuário pode inserir, apagar
# e listar (aparecer todos os valores)

import os
#os.system("cls") -- LIMPA O TERMINAL

lista = []


while True:
    pergunta = input("Você deseja [i]nserir, [a]pagar ou [l]istar: " )
    
    if pergunta.lower() == "i":
        novo_item = input("Digite o item que você quer inserir: ")
        lista.append(novo_item)

    elif pergunta.lower() == "a":
        for indice, valor in enumerate(lista):
            print(indice, valor)

        try:
            indice_apagado = int(input("Qual índice você quer apagar: "))
            lista.pop(indice_apagado)
            for indice, valor in enumerate(lista):
                print(indice, valor)


        except:
            print("Você não digitou um índice válido.")
            continue

    elif pergunta.lower() == "l":
        for indice, valor in enumerate(lista):
            print(indice, valor)


    else:
        input("Você não digitou um comando válido, tente novamente!")
        continue
