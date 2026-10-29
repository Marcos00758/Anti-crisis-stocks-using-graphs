def soma(x):
    def adicao(*args):
        return x + sum(args)
    return adicao

def multiplicacao(x):
    def multiplica(*args):
        total = 1
        for arg in args:
            total *= arg
        return x * total
        
    return multiplica


somar_5 = soma(5)
multiplica_10 = multiplicacao(10)

print(somar_5(10,15,10,12))
print(multiplica_10(15,1))