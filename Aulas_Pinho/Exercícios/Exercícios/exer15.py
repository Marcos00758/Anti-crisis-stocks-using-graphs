#eu entrego números e ele faz virar no estilo cpf
#ex^: 04421962023
vazio = ""

while True:
    cpf = input("Digite seu CPF(apenas números): ")
    if len(cpf) == 11:
        for i in range (0,11,1):
            if i == 3 or i == 6:
                vazio += "." + cpf[i]
            elif i == 9:
                vazio += "-" + cpf[i]
            else:
                vazio += cpf[i]
        break

    elif len(cpf) < 11:
        print("Você digitou menos de 11 dígitos")
        continue
    else:
        print("Você digitou mais de 11 dígitos")
        continue

print(vazio)