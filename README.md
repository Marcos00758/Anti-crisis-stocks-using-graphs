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

## Entrada de Kruskal e Prim

Os algoritmos recebem um DataFrame de distâncias de Mantegna quadrado, não vazio, numérico e simétrico. Linhas e colunas devem conter os mesmos ativos, sem duplicatas e na mesma ordem. Distâncias conhecidas devem estar entre 0 e 2; a diagonal conhecida deve ser zero. A comparação de simetria e diagonal usa tolerância absoluta de `1e-10`.

Valores `NaN` representam distâncias desconhecidas: as arestas correspondentes são ignoradas, sem preencher valores nem excluir ativos automaticamente. Infinitos e outras entradas inválidas geram `ValueError`. Se as arestas conhecidas não conectarem todos os ativos, ambos os algoritmos geram `ValueError` em vez de retornar uma árvore inválida. Prim aceita pesos iguais a 2.

Após alterar as definições, reexecute a célula de importação de NumPy/Pandas e as células de definição de `validar_matriz`/`criar_arestas`, `find`/`union`/`kruskal` e `prim`. A importação de bibliotecas pode ser executada separadamente da linha `%run` para evitar um novo download. Recalcule os resultados antes de interpretar saídas antigas do notebook.
