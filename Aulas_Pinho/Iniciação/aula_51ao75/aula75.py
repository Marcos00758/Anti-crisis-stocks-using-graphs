# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador(numero , vezes):
    return numero * vezes

conta = multiplicador(10,4)
print(conta)

# função dentro de função

def multiplica(vezes):
    def numero(numero):
        return numero * vezes
    return numero

duplica = multiplica(2)
triplica = multiplica(3)
quadruplica = multiplica(4)

print(duplica(4))
print(triplica(15))
print(quadruplica(45))