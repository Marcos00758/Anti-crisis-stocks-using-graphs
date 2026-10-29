nome = "Eduardo Ziegler Berti"
idade = 19
peso_kg = 79
altura = 1.77
imc = peso_kg/(altura**2)

linha1= f"{nome} tem {altura} de altura"
linha2= f'pesa {peso_kg} e seu imc é de {imc:.3f}'

print(linha1)
print(linha2)
print(f"{imc:.3f}")