def deve_ser_int_numero(numero):
    if not isinstance(numero, (int,float)):
        raise TypeError("Você não digitou um número int ou float")

def deve_ser_int_divisor(divisor):
    if not isinstance(divisor, (int,float)):
        raise TypeError("Você não digitou um divisor int ou float")

def divisao_por_zero(divisor):
    if divisor == 0:
        raise TypeError("Você dividiu por zero")


def divide(numero, divisor):

    divisao_por_zero(divisor)
    deve_ser_int_numero(numero)
    deve_ser_int_divisor(divisor)
    
    return numero / divisor

print(divide(15,4))
print(divide(15,"a"))
