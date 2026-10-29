numero_linhas = input("Digite quantas linhas você quer: ")
numero_colunas = input("Digite quantas colunas você quer: ")
numeroc = int(numero_colunas) #adiciona 1, porque o range só iria até ele
numerol = int(numero_linhas)

for x in range(numerol):
    for y in range(1, numeroc + 1):
        print(x,y)
    