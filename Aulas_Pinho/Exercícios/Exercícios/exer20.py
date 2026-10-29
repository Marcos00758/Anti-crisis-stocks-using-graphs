""">>> frase = "Afonso acertou a cerca ontem"
>>> letra = "a"
>>> filtrar_palavras(frase, letra)
['Afonso', 'acertou', 'a', 'cerca']"""

frase = input("Digite a frase: ")
letra = input("Digite a letra especificada: ")

frase_na_lista = frase.split(" ")

lista_palavras_com_criterio = []
for palavra in frase_na_lista:
    if palavra.lower().startswith(letra.lower()):
        lista_palavras_com_criterio.append(palavra)

print(lista_palavras_com_criterio)
