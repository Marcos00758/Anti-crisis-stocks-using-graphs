#calculadora que dobra o número enviado

numero = input("Vou dobrar o número digitado: ")

try:
    numerofloat = float(numero)
    print(f"Float: {numerofloat}")
    print(f"O dobro de {numero} é {numerofloat*2}")
except:
    print("Você não digitou um número. Tente novamente!")