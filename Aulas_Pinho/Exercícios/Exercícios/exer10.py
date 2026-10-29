#verificar se a palavra é palíndromo
while True:
    palindromo = input("Digite uma palavra e direi se é palíndromo: ").lower()
    contrario_palindromo = palindromo[::-1]
    if palindromo == contrario_palindromo:
        print("A palavra escolhida é palindromo.")
        break
    else: 
        print("A palavra escolhida não é palíndromo.")
