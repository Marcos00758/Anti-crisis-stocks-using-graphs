# fazer o seu nome ficar assim:
# Eduardo - *E*d*u*a*r*d*o
# Essa é a minha solução, não sabendo como concatenar
nome = input("Digite seu nome: ")
quantidade_letras = len(nome)
comeco = 0

while comeco < quantidade_letras:
    print("*", nome[comeco])
    comeco += 1
    continue

#Essa é a solução certa vista depois do professor
nome1 = input("Digite seu nome: ")
inicio = 0 
novo_nome = ""

while inicio < len(nome1):
    novo_nome += f"*{nome1[inicio]}"
    inicio += 1
    continue
novo_nome += "*"
print(novo_nome)