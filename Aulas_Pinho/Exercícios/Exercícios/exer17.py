palavra = ("Cimento").lower()
segredo = len(palavra) * "*"
tentativas = 0
vazio = ""
import os

while True:
    letra_escolhida = input("Digite uma letra: ").lower()
    i = 0

    if letra_escolhida.isalpha():
        if len(letra_escolhida) == 1:
            if letra_escolhida not in segredo:
                for letra in palavra:
                    if palavra[i] == letra_escolhida:
                        vazio += palavra[i]
                        i += 1

                    else:
                        vazio += segredo[i]
                        i += 1

                tentativas += 1
                segredo = vazio

                if segredo != palavra:
                    print(segredo.capitalize())
                    vazio = ""
                    print(f"Você já fez {tentativas} tentativas!")
                
                elif segredo == palavra:
                    os.system("cls")
                    print(f"Você acertou a palavra: {segredo.capitalize()}")
                    print(f"Parabéns, você usou {tentativas} tentativas!")
                    break

            elif letra_escolhida in segredo:
                print("Você já digitou essa letra")

        elif not letra_escolhida:
            print("Você não digitou nenhuma letra")

        else:
            print("Você digitou mais de uma letra")

    else:
        print("Você digitou números!")