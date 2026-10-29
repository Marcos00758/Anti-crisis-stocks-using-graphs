"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9 #só poderia ser de 0 a 10, 
então se for 10 é 0
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpfstr = input("Digite um CPF: ")
resultado = 0
i = 0

for multiplicador in range(10,1,-1):
    resultado += int(cpfstr[i]) * multiplicador
    i += 1
    print(resultado)

resultado_final = resultado * 10
print(resultado_final)
divisao = resultado_final % 11
print(divisao)

if divisao == 10:
    print("O primeiro dígito do CPF é 0")
else:
    print(f"O primeiro dígito do CPF é {divisao}")
    