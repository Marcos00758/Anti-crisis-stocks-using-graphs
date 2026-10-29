mao = ["Copas", "Ouros", "Espadas", "Ouros", "Copas", "Paus", "Espadas", 
       "Copas", "Ouros", "Paus", "Paus", "Copas", "Espadas", "Ouros", 
       "Copas", "Copas", "Paus", "Ouros", "Espadas", "Ouros", "Copas", "Paus"]

def conta_naipe(lista):
    dicionario = {}
    for naipe in lista:
        contador = lista.count(naipe)
        if contador > 3:
            contador *= 2
        dicionario[naipe] = contador
    
    return dicionario

print(conta_naipe(mao))