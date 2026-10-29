#Gerador de CPF
import random

digitos_9 = random.randint(100000000, 999999999)
multiplicador = 10
soma1, soma2 = 0,0

for numero in str(digitos_9):
    soma1 += int(numero) * multiplicador
    multiplicador -= 1

primeiro_digito = (soma1*10) % 11
if primeiro_digito == 10:
    primeiro_digito = 0
else:
    primeiro_digito = primeiro_digito

digitos_10 = str(digitos_9) + str(primeiro_digito)

multiplicador = 11
for numero in digitos_10:
    soma2 += int(numero) * multiplicador
    multiplicador -= 1

segundo_digito = (soma2*10) % 11
if segundo_digito == 10:
    segundo_digito = 0

print(str(digitos_10)+str(segundo_digito))