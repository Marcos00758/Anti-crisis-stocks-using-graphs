secreta = "Tema"
qtd_letras_secreta = len(secreta)
print("Tente acertas as letras da palavra secreta!!!")
erros = 0
i = 0

while True:
    letra = input(f"{i+1}°letra: ").lower()

    if i >= qtd_letras_secreta - 1:
        print(f"Você acertou toda a palavra {secreta}")
        break

    if letra == secreta[i].lower():
        print("Você acertou a letra!")
        i += 1
    
    else:
        erros += 1
        print(f"Você errou {erros} vezes, tente novamente!")
        continue
