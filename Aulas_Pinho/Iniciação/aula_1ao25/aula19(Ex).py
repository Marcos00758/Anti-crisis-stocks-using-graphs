#dar dois valores e colocar, o valor (1 ou 2) é maior do que o valor (o que sobrou)
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro = float(primeiro_valor)
segundo = float(segundo_valor)

if primeiro == segundo:
    print(f"O primeiro valor {primeiro}" 
    "é igual ao segundo valor {segundo}"
    )
    
elif primeiro > segundo:
    print(f"O primeiro valor {primeiro} é maior ao segundo valor {segundo}")

else:
    print(f"O segundo valor {segundo} é maior ao primeirovalor {primeiro}")
