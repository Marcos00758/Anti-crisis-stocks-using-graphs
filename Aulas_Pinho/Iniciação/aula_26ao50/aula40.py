#calculadora com While
"""1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Sair"""

operacaonumero = None
operacaosinal = None
final = ""

while True:
    operacaonumero = input("Digite um número: ")
    final += operacaonumero
    operacaosinal = input("Digite um sinal (+, -, *, / e sair): ")
    if operacaosinal != "sair":
        final += operacaosinal
    else:
        break

print(eval(final))

#Calculadora do curso
#pede dois valores e a operação matemática

equaçao1 = input("Digite o 1° número:")
sinal = input("Digite o sinal:")
equaçao2 = input("Digite o 2° número:")

try:
    if sinal == "+":
        print(float(equaçao1) + float(equaçao2))
    elif sinal == "-":
        print(float(equaçao1) - float(equaçao2))
    elif sinal == "*":
        print(float(equaçao1) * float(equaçao2))
    elif sinal == "/":
        print(float(equaçao1) / float(equaçao2))
except:
    print("Você digitou algo errado.")