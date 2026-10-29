#eu entrego números e ele faz virar no estilo cpf
#ex^: 04421962023
while True:

    cpf = input("Digite seu CPF:")

    if len(cpf) == 11 and cpf.isdigit():
        cpf_formatado = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
        print(cpf_formatado)
        break

    if len(cpf) < 11:
        if not cpf.isdigit():
            print("Você digitou menos de 11 dígitos e digitou letras")
            continue
        
        else:
            print("Você digitou menos de 11 dígitos")
            continue

    else:
        if not cpf.isdigit():
            print("Você digitou mais de 11 dígitos e digitou letras")
            continue

        else:
            print("Você digitou mais de 11 dígitos")
            continue