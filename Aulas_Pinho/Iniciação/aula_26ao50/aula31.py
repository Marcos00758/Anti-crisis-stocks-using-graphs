condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True #aqui ele muda o nome
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if') 