# criar um senha e deixar o usuário ter 3 tentativas para descobri-la

senha = "12345"
tentativas = 0
print("A senha é *****! Você pode errar 3x antes de ser bloqueado.")

while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha:
        print("Você acertou a senha, pode entrar!")
        break
    else:
        tentativas += 1
        tentativas_restantes = 3 - tentativas
        if tentativas_restantes == 0:
            print("Você não tem mais tentativas. Foi bloqueado.")
            break
        else:
            print(f"Senha incorreta. Você tem mais {tentativas_restantes} chances)")
    