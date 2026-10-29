contador = 0

while contador <= 100:
    contador += 1

    if contador > 5 and contador < 24:
        print(f"Não aparecia o {contador}")
        continue

    if contador == 50:
        print(contador) #sempre será o 50
        break #ele quebra antes do 100, agora vai só até o 50
    
    print(contador) 