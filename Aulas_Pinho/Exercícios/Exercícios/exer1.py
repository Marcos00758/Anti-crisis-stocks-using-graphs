peso = input("Qual é seu peso (em kg): ")
altura = (input("Qual é sua altura (em m): "))

pesoint = float(peso)
alturaint = float(altura)

imc = pesoint/alturaint**2

print(f"Seu IMC é de: {imc:.2f}")