string = "Inteiro"

contador = 0
while contador < len(string):
    if string[contador] == " ": 
        break
    print(string[contador])
    contador += 1
else: 
    print(f"A palavra {string}")

string1 = "Espaços incluídos"

contador1 = 0
while contador1 < len(string1):
    if string1[contador1] == " ": 
        break
    print(string1[contador1])
    contador1 += 1
else: 
    print(f"A palavra inteira é: {string1}")
    
    
