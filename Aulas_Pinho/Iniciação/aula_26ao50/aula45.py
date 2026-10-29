numeros = range(5,10)
vazio = ""
for numero in numeros:
    vazio += f"{numero} , "

vazio = vazio[:-3] #tira os dois últimos caracteres
print(vazio)