"""Fazer uma calculadora de 2 números e mostrar o resultado """
valor1 = input("Digite o primeiro número: ")
sinal = input("Digite o sinal desejado ou escreva: +, -, * ou /: ")
valor2 = input("Digite o segundo número: ")

fvalor1 = float(valor1)
fvalor2 = float(valor2)

if sinal == "+" or "mais" or "soma":
    print(fvalor1 + fvalor2)
elif sinal == "-" or "subtração" or "menos":
    print(fvalor1 - fvalor2)
elif sinal == "*" or "multiplicação" or "vezes":
    print(fvalor1 * fvalor2)
elif sinal == "/" or "divisão":
    print(fvalor1 / fvalor2)
else:
    print("Você digitou um símbolo inválido")