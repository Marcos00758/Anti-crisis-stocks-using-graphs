#Contexto: Você tem uma base de dados de temperaturas diárias de uma cidade. O problema é que o 
# sensor quebrou algumas vezes, registrando um valor absurdo (-999.0). Você precisa calcular a 
# temperatura média da cidade, mas antes disso, você deve limpar a lista: toda vez que encontrar 
# um -999.0, você deve substituí-lo pela temperatura do dia anterior

temperaturas = [22.5, 23.0, 24.1, -999.0, 25.5, 26.2, -999.0, -999.0, 24.8, 23.9]

for indice, temperatura in enumerate(temperaturas):
    if temperatura == -999.0:
        if indice == 0:
            temperaturas[indice] = 0
        else:
            temperaturas[indice] = temperaturas[indice - 1]

print(temperaturas)
