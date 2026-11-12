# Matemática discreta e finanças

## Carregar os dados das ações

1. Abra `Algoritimos.ipynb` no Jupyter ou no VS Code com suporte a notebooks Python.
2. Use a pasta deste projeto como diretório de trabalho do kernel.
3. Execute as células em ordem. A célula `%run ./Tabelas_Acoes.ipynb` executa o notebook de dados e disponibiliza as tabelas no notebook de algoritmos.

O notebook de dados instala `yfinance` e consulta o Yahoo Finance e o Banco Central. É necessário ter internet; o download pode demorar e depende da disponibilidade desses serviços. Cada execução dessa célula consulta os dados novamente.

Após a execução, use estas variáveis nas próximas células:

| Variável | Conteúdo |
| --- | --- |
| `df` | Preços e volumes das ações |
| `variacao_diaria` | Variação diária percentual dos preços de fechamento |
| `variacao_logaritma` | Retornos logarítmicos das colunas de `df` |
| `preco_real` | Preços de fechamento corrigidos pelo IPCA |

Por exemplo, execute `variacao_diaria.head()` em uma nova célula para conferir as primeiras linhas. Para consultar os preços de fechamento, use `df['Close'].head()`.
