vogais = "aeiouãõâêîûôáéíóúàèìòùãõ"
frase = input("Digite a sua frase: ").lower()
contagem_vogais = 0
espacos_vazios = frase.count(" ")

for letra in frase:
    if letra in vogais:
       contagem_vogais += 1

consoantes = (len(frase) - espacos_vazios - contagem_vogais)
print(f"Vogais: {contagem_vogais}",f"Consoantes: {consoantes}")