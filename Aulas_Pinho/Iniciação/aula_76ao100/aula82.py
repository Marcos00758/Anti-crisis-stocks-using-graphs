s = set()
tentativas = 0
letra_secreta = "h"

print("Tente adivinhar a letra secreta:")

while True:
    letra = input("Digite a letra: ").lower()

    if letra in s:
        print("Você já digitou essa letra")
    
    elif len(letra) > 1:
        print("Digite apenas uma letra!")
    
    elif letra == letra_secreta:
        print("Parabéns, você acertou a palavra certa!")

    else:
        tentativas += 1
        s.add(letra)
        print(f"Letras digitadas: {sorted(s)}")
        print(f"Número de tentativas: {tentativas}")
    
    print()

