frases = " Eduardo Berti "
print(frases)
print(frases.strip())

frase_nova = "Bom dia, pessoal"
lista_frase = frase_nova.split(",")

for i, frase in enumerate(lista_frase):
    lista_frase[i] = lista_frase[i].strip()

print(lista_frase)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)