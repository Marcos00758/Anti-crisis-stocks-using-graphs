frase = "Algo poderoso que aprendi enquanto programador e que" \
        " devemos aplicar na realidade é: ERRAR RÁPIDO!"
i = 0 # índice
fraseminuscula = frase.lower()
print(fraseminuscula)

maiorquantidade = 0
maiorletra = ""

while i < len(frase):
    letra_atual = fraseminuscula[i]
    quantidadeletras = fraseminuscula.count(letra_atual)
    print(letra_atual, quantidadeletras)
    
    if letra_atual == " ":
        i += 1
        continue

    elif quantidadeletras > maiorquantidade:
        maiorquantidade = quantidadeletras
        maiorletra = letra_atual
    
    i += 1

print(f"A letra que mais aparece é '{maiorletra.upper()}' com {maiorquantidade}x")
