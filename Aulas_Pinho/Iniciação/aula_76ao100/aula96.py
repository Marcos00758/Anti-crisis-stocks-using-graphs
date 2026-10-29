try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except Exception as error:
    print(error)
    print(error.__class__.__name__)
    
print('CONTINUAR')