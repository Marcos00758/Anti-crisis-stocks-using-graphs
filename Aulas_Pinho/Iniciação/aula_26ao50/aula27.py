#FATIAMENTO DE STRINGS

#fatiamento [inicio:fim(Não pega o último elemento):contar de qto em qto]
# se deixar em branco é o mesmo que colocar 0 ex: [:5], ele começa do início
#[5:] vai até o final
#[5] pega só o 5

#           012345678
variavel = "123456789"
#          -987654321 (São todos negativos)
print(variavel[3])
print(variavel[3:8])
print(variavel[3::2])
print(variavel[:2:1])
print(len(variavel[:2:1])) #Aqui ele conta 2 apenas
print(len("0123456789"))
print()
print(variavel[::-1]) #conta de trás para frente
