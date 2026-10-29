""" Contador de letras mais frequentes
- Peça uma frase ao usuário.
- Conte qual letra aparece mais vezes usando while.
- Ignore espaços e pontuação.
- Exiba a letra mais frequente e sua quantidade."""

frase = input("Digite uma frase e direi qual letra mais aparece nela: ").lower()
i = 0
numero_letras = len(frase)
maior_quantidade = 0
letra_mais_aparece = None

while i < numero_letras:
    letraatual = frase[i]
    quantidade_atual = frase.count(letraatual)

    if letraatual == " ":
        i += 1
        continue

    elif quantidade_atual > maior_quantidade:
        letra_mais_aparece = letraatual
        maior_quantidade = quantidade_atual

    i += 1
    
print(f"A letra que mais aparece é a letra *{letra_mais_aparece.upper()}* com *{maior_quantidade}* vezes")