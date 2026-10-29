palavra = "TEnTadoR"
segredo = palavra.lower()
palavra_final = "*" * len(segredo)
tentativas = 0

while True:
    vazia = ""
    letra = input("Digite uma letra: ").lower()

    if len(letra) > 1:
        print("Você digitou mais de uma letra")
        tentativas += 1
        continue

    else:
        tentativas += 1
        for i in range(len(segredo)):
            if segredo[i] == letra:
                vazia += letra
            else:
                vazia += palavra_final[i]

    palavra_final = vazia
    print(palavra_final)

    if palavra_final == segredo:
        break

print(f"Você acertou a palavra {palavra_final} em {tentativas} tentativas!")