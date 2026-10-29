segredo = "tentativa"
palavra_escondida = "*" * len(segredo)
tentativas = 0

while True:
    letra = input("Digite uma letra: ").lower()
    if len(letra) > 1:
        print("Você digitou mais de uma letra.")
        continue
    
    vazia = ""
    for i in range(len(segredo)):
        if segredo[i] == letra:
            vazia += letra
        else:
            vazia += palavra_escondida[i]

    tentativas += 1
    palavra_escondida = vazia
    print(palavra_escondida)
    
    if palavra_escondida == segredo:
        print(f"Você acertou a palavra em {tentativas} tentativas!")
        break