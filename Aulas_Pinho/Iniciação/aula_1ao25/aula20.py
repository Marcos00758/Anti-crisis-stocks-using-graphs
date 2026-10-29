entrada = input('Para entrar digite "E", para sair digite "S": ')
if entrada == "E":
    senha = input("Digite sua senha: ")
    if entrada == "E" and senha == "123":
        print("Você entrou no sistema.")
    elif entrada == "E" and senha != "123":
        print("A senha digitada está errada.")

if entrada != "E":
    print("Você saiu do sistema.")

