pessoa = {'nome' : 'Eduardo Ziegler Berti',
'idade' : "19 anos",
'endereço' : "Rua Luiz Olindo Berti, 722"}

print(pessoa['nome'],"\n" + pessoa['endereço'])
print()

for parametro in pessoa:
    print(parametro, "=", pessoa[parametro])

print(pessoa.get('nome', "Não existe"))

if pessoa.get("sexualidade") is None:
    print("Não existe")
else:
    print("Existe")