lista = [1,2,3,4,5,6,7,8,9,10]
iteravel = iter(lista)

while True:
    
    try:
        print(next(iteravel))

    except:
        break