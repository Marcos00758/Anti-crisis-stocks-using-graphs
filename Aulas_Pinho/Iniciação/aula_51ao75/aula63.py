# o segundo dígito do cpf

cpfstr = input("Digite um CPF: ")
resultado = 0
i = 0

for multiplicador in range(11,1,-1):
    resultado += int(cpfstr[i]) * multiplicador
    i += 1

resultado_final = resultado * 10
divisao = resultado_final % 11

if divisao == 10:
    print("O segundo dígito do CPF é 0")
else:
    print(f"O segundo dígito do CPF é {divisao}")
    