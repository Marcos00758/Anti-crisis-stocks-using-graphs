#pedir frases e uma letra proibida, se a frase tiver a letra proibida, avisa
while True:
    frase = input("Digite uma frase ou palavra: ")
    caracter_proibido = input("Digite um caracter proibido ou 'sair' para SAÍDA: ")
    frase_minuscula = frase.lower()
    proibido = caracter_proibido.lower()
    if proibido == "sair" or frase == "sair":
        break
    elif len(proibido) > 1:
        print("Você digitou mais de um caracter")
    elif proibido in frase_minuscula:
        print("Essa frase contém o caracter proibido!")
    elif proibido not in frase_minuscula:
        print("Essa frase NÃO contém o caracter proibido, sendo válida.")