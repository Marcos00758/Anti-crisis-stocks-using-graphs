#Os itens da string podem ser contadas de forma positiva (0,1,2,3,4...)
#Ou de forma negativa que é de trás para frente(...-5,-4,-3,-2,-1)
# 0 1 2 3 4 5 6
# E D U A R D O
#-7-6-5-4-3-2-1
#para acessar isso, usa-se o [índice]
nome = "Eduardo"

print(nome[1])
print(nome[-6])
print("e" in nome) #reconhece minúsculas e maiúsculas
print("E" in nome)
print("Edu" in nome)

palavra = input("Digite uma palavra: ")
encontrar = input("O que deseja encontrar que está dentro da palavra: ")

if encontrar in palavra:
    print(f"{encontrar} está em {palavra}")
elif encontrar not in palavra: #daria para usar um else:
    print(f"{encontrar} não está em {palavra}")
