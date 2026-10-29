#contador de vogais

frase = "Apesar de todas as adversidades que enfrentamos diariamente, a persistência e a dedicação aos nossos sonhos continuam sendo as ferramentas mais poderosas que possuímos para transformar completamente a nossa realidade e alcançar o sucesso que tanto almejamos para o nosso futuro."

def conta_vogais(f):
    dicionario = {}
    vogais = 'AEIOU'

    for vogal in vogais:
        contador = f.upper().count(vogal)
        dicionario[vogal] = contador

    return dicionario



def conta_consoantes(f):
    dicionario = {}
    letras = 'BCDFGHJKLMNPQRSTVWXYZ'

    for letra in letras:
        contagem_letra = f.upper().count(letra)
        if contagem_letra > 0:
            dicionario[letra.upper()] = contagem_letra

    return dicionario

print(conta_vogais(frase))
print(conta_consoantes(frase))


