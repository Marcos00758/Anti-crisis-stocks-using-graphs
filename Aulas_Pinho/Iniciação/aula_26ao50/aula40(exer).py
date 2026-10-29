#Calculadora do curso
#pede dois valores e a operação matemática
#pede se a pessoa quer sair, se ela não quiser continua fazendo novas operações

while True:
    sair = input("Deseja sair [s] ou [n]? ").lower().startswith('s')
    if sair:
        print("Você saiu!")
        break
    else:
        operacao1 = input("Digite o 1° número: ")
        operacao2 = input("Digite o 2° número: ")
        sinal = input("Digite o operador (+, -, / ou *): ")
        try:
            valor1 = float(operacao1)
            valor2 = float(operacao2)
            sinaisvalidos = ["+", "-", "*", "/"]
            if sinal not in sinaisvalidos:
                print("Você digitou o operador errado!")
            elif sinal == "+":
                print(valor1 + valor2)
            elif sinal == "-":
                print(valor1 - valor2)
            elif sinal == "*":
                print(valor1 * valor2)
            elif sinal == "/":
                if operacao2 == "0":
                    print("Divisão por zero não existe.")
                else:
                    print(valor1 / valor2)
        except: 
            print("Você digitou um dos números errados!")

