texto = iter("Eduardo")

print(next(texto))
print(next(texto))
print(next(texto))

nomes = "Ana", "Beto", "Carlos"
it = iter(nomes)
print("")
print("Oi,",next(it))
print(next(it))
print(next(it))

mensagem = iter("Oi")

while True:
    try:
        print(next(mensagem))   # imprime 'O' e 'i'
    except:
        break


