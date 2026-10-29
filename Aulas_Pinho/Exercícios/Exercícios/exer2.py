"""Crie um programa que faça as seguintes perguntas ao usuário:
Qual é o seu nome? (Texto)
Qual é a sua idade? (Número inteiro)
Qual é a sua altura em metros? (Número decimal, ex: 1.75)
Saída esperada: O programa deve exibir uma frase final formatada usando f-string, parecida com esta:
"Olá, [Nome]. Você tem [Idade] anos e mede [Altura] metros."""

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
altura = input("Qual é a sua altura? ")

idadeint = int(idade)
alturafloat = float(altura)

print(f"Olá, {nome}. Você tem {idadeint} anos e mede {alturafloat} metros")