valor = 100.0 #é divisível por todos os números de 1 a 12
parcelas = input("Digite o número de parcelas (apenas o número): ")
vezes = int(parcelas)
i = 1
valorparcela = (valor/vezes)
selicstr = input("Qual a taxa selic anual mensal (decimal): ")
selic = float(selicstr)

while i <= vezes:
    novosaldo = 0
    valor = (valor-valorparcela)*selic
    novo_valor = valor
    valor = float(novo_valor)
    valor = float(novo_valor)
    i += 1

print(f"{valor:.3f}")
if vezes <= 6:
    recebido_sem_imposto = valor*0.775 #tirando o imposto
elif vezes <= 12:
    recebido_sem_imposto = valor*0.8
elif vezes <= 24:
    recebido_sem_imposto = valor*0.825
print(f"{recebido_sem_imposto = :.3f}")

descontopreco = (valor - recebido_sem_imposto)

descontoreal = 100*(descontopreco/valor)
print(f"O desconto deve ser de, NO MÍNIMO, {(100-descontoreal):.2f}% para comprar no pix.")
print(f"")

