senha_digitada = input("Digite a sua senha: ")
senha_correta = "123"
repeticoes = 1

while senha_digitada != senha_correta:
    print(f"A sua senha deu errado pela {repeticoes}x")
    senha_digitada = input("Digite a sua senha novamente: ")
    repeticoes += 1 
else: 
    print("A sua senha foi aprovada!")

# LAÇOS COM WHILE: eu posso errar a senha infinitamente
# laços com while: usado para quando precisa-se de possíveis rep infinitas

texto = input("Digite o texto desejado: ")
novotexto = "*"
textosemestrelas = ""

for letra in texto: 
    novotexto += f"{letra}*"
    textosemestrelas += f"{letra}"
print(f"O texto é {textosemestrelas}")
print(novotexto)