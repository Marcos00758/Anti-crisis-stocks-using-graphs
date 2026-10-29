# Exercícios com funções
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = mult(1,2,3,4,5,6)
print(f'A multiplicação resultou em: {multiplicacao}')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def paridade(x):
    valor = (x % 2)

    if valor == 0:
        print(f'O valor {x} é par')
    else:
        print(f'O valor {x} é ímpar')

paridade(10)
paridade(15)