def soma(*args):
    total = 0
    for numero in args:
        total += numero
    print(f'A soma é {total}')

soma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

def somareturn(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma1 = somareturn(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
print(soma1)