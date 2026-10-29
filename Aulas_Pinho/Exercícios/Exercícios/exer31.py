#Objetivo: Encontrar o índice exato onde ocorreu o maior Erro Quadrático 
# ( $(Previsto - Real)^2$ ), programando a lógica de "busca de máximo" do zero 
# com as variáveis maior_erro e indice_do_pior_erro.

valores_reais = [
    15.5, 20.0, 18.2, 30.5, 12.1, 45.0, 10.2, 22.8, 31.4, 19.9,
    14.5, 27.6, 33.3, 11.0, 21.5, 40.2, 17.8, 25.4, 29.1, 16.6
]

valores_previstos = [
    15.0, 22.1, 18.2, 25.0, 10.0, 42.5, 12.0, 22.0, 31.0, 24.5,
    14.0, 30.0, 28.5, 11.5, 20.0, 35.8, 18.5, 25.0, 32.0, 15.0
]


lista_erro = []
for real, previsto in zip(valores_reais, valores_previstos):
    erro = (previsto - real)**2
    lista_erro.append(erro)

maior_erro = 0
indice_maior = 0

for i in range(len(lista_erro)):
    if lista_erro[i] > maior_erro:
        maior_erro = lista_erro[i]
        indice_maior = i

print(f'O maior erro é:{maior_erro}, que aconteceu no {indice_maior}° indice')
