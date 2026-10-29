texto = "o sucesso é a soma de pequenos esforços"
numero_vezes = 0
letra_aparece = None
for letra in texto:
    qtd_aparece = texto.count(letra)
    if letra == " ":
        continue
    elif qtd_aparece > numero_vezes:
        numero_vezes = qtd_aparece
        letra_aparece = letra
print(f"A letra que mais aparece é {letra_aparece} com {numero_vezes} vezes!")