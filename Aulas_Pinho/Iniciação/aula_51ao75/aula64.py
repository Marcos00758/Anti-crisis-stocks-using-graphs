#verificador de validação de CPFs

cpf = input("Digite o CPF (apenas números): ")
resultado = 0
i = 0

for multiplicador in range(10, 1, -1):
    resultado += int(cpf[i]) * multiplicador
    i += 1

resultado_final1 = (resultado*10) % 11

i = 0
resultado = 0
for multiplicador2 in range(11,1, -1):
    resultado += int(cpf[i])*multiplicador2
    i += 1

resultado_final2 = (resultado * 10) % 11

if resultado_final1 == int(cpf[-2]) and resultado_final2 == int(cpf[-1]):
    print(f'CPF "{cpf}" é válido!')
else:
    print("O CPF é inválido!")
    