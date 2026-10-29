'''Peça ao usuário para digitar a Nota 1.
Peça ao usuário para digitar a Nota 2.
Calcule a média (nota1 + nota2) / 2.
Exiba a média na tela.
Regra de decisão:
Se a média for maior ou igual a 7: Imprima "Aprovado".
Se a média for menor que 7: Imprima "Reprovado".'''

nota1 = input("Digite a nota da prova 1 (0 a 10): ")
nota2 = input("Digite a nota da prova 2 (0 a 10): ")

nota1f = float(nota1)
nota2f = float(nota2)

media = (nota1f + nota2f)/2

if media >= 7:
    print("Você foi aprovado!")
else:
    print("Você não atingiu a média esperada.")