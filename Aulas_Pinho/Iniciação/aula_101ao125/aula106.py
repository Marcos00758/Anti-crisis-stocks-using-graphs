def soma(*args):
    total = sum(args)   # soma todos os argumentos
    def adicao(y):
        return total + y
    return adicao

somar_5 = soma(5)          # total = 5
print(somar_5(10))         # 5 + 10 = 15
