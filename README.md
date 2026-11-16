# Matemática discreta e finanças

Quando o notebook for alterado externamente, preserve suas edições não salvas e reabra o arquivo para carregar a versão do disco. Em um conflito de salvamento, `Overwrite` pode gravar a versão antiga da aba sobre as alterações externas; compare ou recarregue as versões antes de salvar.

## Carregar os dados das ações

1. Abra `Algoritimos.ipynb` no Jupyter ou no VS Code com suporte a notebooks Python.
2. Use a pasta deste projeto como diretório de trabalho do kernel.
3. Execute as células em ordem. A célula `%run ./Tabelas_Acoes.ipynb` executa o notebook de dados e disponibiliza as tabelas no notebook de algoritmos.

O notebook de dados instala `yfinance` quando necessário e consulta o Yahoo Finance e o Banco Central. Na primeira execução sem coleta local, o download das ações exige internet e pode demorar. Nas execuções seguintes, os preços são carregados da cópia local. A seção de IPCA continua consultando o Banco Central e exige internet mesmo quando os preços já estão salvos.

Após a execução, use estas variáveis nas próximas células:

| Variável | Conteúdo |
| --- | --- |
| `df` | Preços e volumes das ações |
| `variacao_diaria` | Variação diária percentual dos preços de fechamento |
| `variacao_logaritma` | Retornos logarítmicos das colunas de `df` |
| `preco_real` | Preços de fechamento corrigidos pelo IPCA |

Por exemplo, execute `variacao_diaria.head()` em uma nova célula para conferir as primeiras linhas. Para consultar os preços de fechamento, use `df['Close'].head()`.

## Experimento da pandemia — etapa 1

O escopo desta parte é implementar a MST, calcular métricas estruturais e selecionar ativos. Simulação das carteiras, benchmarks, métricas de risco, análise financeira e visualizações gráficas ficam com outro integrante. O plano incremental está em [PLANO_ALGORITMOS.md](PLANO_ALGORITMOS.md).

As datas estão centralizadas em `parametros_experimento.json`. Ambos os notebooks têm, no início, uma seção **Etapa 1 - Parametros do experimento da pandemia**, cuja célula carrega as datas e mostra a pasta da coleta. Ela funciona sozinha, sem instalar bibliotecas nem consultar serviços externos. Para localizar as mudanças, procure por esse título; as saídas antigas não são atualizadas até a célula ser executada.

| Parâmetro | Valor | Significado |
| --- | --- | --- |
| `inicio_formacao` / `fim_formacao` | 2017-01-01 / 2019-12-31 | Janela proposta para construir a MST |
| `inicio_avaliacao` / `fim_avaliacao` | 2020-01-01 / 2022-12-31 | Janela para acompanhar as carteiras |
| `inicio_historico` / `fim_historico_exclusivo` | 2008-01-01 / 2026-01-01 | Histórico solicitado ao Yahoo; o fim é exclusivo |
| `pasta_coleta` | `dados/pandemia` | Local da cópia persistida dos dados |

A etapa 1 define os períodos e preserva a coleta. As etapas 2–5 usam os retornos elegíveis de 2017–2019 para calcular Pearson, Mantegna, a MST de Kruskal e as métricas estruturais. Seleção dos ativos e exportação permanecem nas etapas 6 e 7. O período 2020–2022 é apenas uma referência para a entrega ao outro integrante; sua simulação financeira não será implementada aqui.

Na primeira execução, a célula que define `baixar_acoes` salva:

- `dados/pandemia/acoes.csv`: o DataFrame `df`, incluindo preços OHLC ajustados e volumes, antes dos cálculos de retornos ou IPCA. O CSV tem duas linhas de cabeçalho (`Price`, `Ticker`) e a primeira coluna contém as datas. Os valores ausentes são preservados.
- `dados/pandemia/metadados.json`: início e fim da coleta em UTC, fonte, parâmetros, ações solicitadas, ações com/sem fechamento, datas efetivas, dimensões da base, versões das bibliotecas e hash SHA-256 do CSV.

Nas próximas execuções, a mesma célula verifica o hash e carrega `acoes.csv` com `header=[0, 1]`, `index_col=0`, `parse_dates=True` e `float_precision='round_trip'`, sem consultar novamente a lista de ações ou baixar preços. Cada chamada de `baixar_acoes` cria sua própria lista de lotes, evitando acumular resultados de chamadas anteriores.

A coleta não é sobrescrita automaticamente. Para uma nova coleta, escolha outra `pasta_coleta` no arquivo de parâmetros e mantenha a pasta anterior. Se o período histórico mudar sem mudar a pasta, o notebook informa o conflito. Um CSV alterado ou uma coleta com apenas um dos dois arquivos também gera erro, sem apagar os arquivos existentes. Mensagens de falha do Yahoo devem ser revisadas; uma cópia salva não significa que todas as ações tenham histórico suficiente.

Para conferir apenas as datas, execute a célula da seção **Etapa 1** em qualquer um dos notebooks. Para obter ou reutilizar os dados, execute primeiro essa célula e depois as células de importação e coleta de `Tabelas_Acoes.ipynb`, na ordem. Confira a mensagem de gravação, os dois arquivos e as datas nos metadados. Ao executar a célula de coleta novamente, deve aparecer a mensagem de carregamento local. As saídas antigas dos notebooks não comprovam a execução dessa nova versão. A criação da cópia exige executar a célula de dados; os dados completos do kernel não ficam disponíveis apenas pelas saídas resumidas do notebook.

O IPCA não faz parte desta cópia congelada. O experimento principal usará retornos de preços ajustados por eventos corporativos, sem deflação pelo IPCA. O retorno real das carteiras poderá ser apresentado na avaliação, como medida de poder de compra. A ramificação existente de IPCA foi preservada, mas ainda precisa de revisão: hoje correlaciona níveis de preços corrigidos e aplica um índice mensal em degraus, em vez de calcular retornos reais com uma convenção temporal explícita.

## Etapa 2 — Elegibilidade da formação

Em `Algoritimos.ipynb`, procure a seção **Etapa 2 - Elegibilidade e retornos da formacao (2017-2019)**, antes das matrizes. Com `df` e `acoes` já carregados e NumPy/Pandas importados, execute a célula que define `preparar_formacao` e a seguinte, que mostra a tabela. A célula lê os parâmetros novamente sem repetir downloads.

A cobertura mínima de 90% está em `cobertura_minima_formacao` no JSON. Conforme escolha do usuário, o denominador é, provisoriamente, a quantidade de datas presentes na base entre o início e o fim da formação, não um calendário oficial. A função permite passar uma lista de datas em `sessoes` quando houver um calendário definido. As datas existentes são mantidas mesmo quando todos os fechamentos daquela data estão ausentes; sessões inteiramente ausentes do índice não podem ser identificadas por essa referência.

Os fechamentos são limitados ao fim de 2019 antes da análise, e os retornos são calculados por diferença dos logaritmos dos preços positivos e finitos. O fechamento anterior a 2017 pode ser usado no primeiro retorno. Nenhum preço é preenchido e `df` não é alterado. Preços não positivos ou infinitos são contados e desconsiderados nos cálculos, com pendência de investigação.

As situações são:

- `Elegivel`: cobertura mínima atendida, pelo menos dois retornos, variância positiva e finita, evidência de preço até a primeira sessão e preço na última sessão da formação, sem preços inválidos na janela. Isso não comprova a data oficial de listagem.
- `Excluida`: cobertura insuficiente, menos de dois retornos ou variância nula/indefinida. Os motivos são registrados, sem atribuir a ausência de dados automaticamente a IPO recente ou deslistagem.
- `Pendente`: atende aos critérios numéricos, mas falta evidência no início, preço na última sessão ou há preços inválidos que exigem investigação. Essas ações não entram na seleção provisória.

As saídas são `tabela_elegibilidade`, `retornos_formacao`, `acoes_elegiveis` e `retornos_formacao_elegiveis`. Para investigar, consulte `tabela_elegibilidade.loc['AXIA7.SA']` se esse ticker estiver presente, ou filtre por `Situacao`. Não há CSV novo nesta etapa; a exportação será feita na etapa 7. O universo histórico e mudanças de ticker continuam dependendo de conferência com o responsável pelos dados.

Confira a tabela de elegibilidade antes de prosseguir. As células seguintes já estão integradas à entrada da formação; saídas antigas precisam ser recalculadas.

## Etapas 3, 4 e 5 — Matrizes, MST e métricas

Pearson usa `retornos_formacao_elegiveis` com mínimo de observações conjuntas definido por `proporcao_minima_observacoes_conjuntas` no JSON, inicialmente 80% das datas da formação, arredondado para cima. As matrizes resultantes são `matriz_correlacoes_formacao` e `matriz_mantegna_formacao`. Não há exclusão manual de `RENT4.SA`; sua participação depende da elegibilidade. A ramificação de IPCA é exploratória e não alimenta a MST.

Kruskal recebe `matriz_mantegna_formacao` e mantém `mst_kruskal` e `peso_kruskal` como saídas. A função de Prim foi preservada, mas sua chamada continua comentada. Nenhuma validação ou teste novo foi acrescentado; as verificações existentes continuam nas funções.

Na etapa 5, `metricas` apresenta índice do vértice, ticker, grau, excentricidade, indicação de folha e indicação de centro. Os tickers usam a mesma matriz e ordem de índices da MST. `diametro` e `centro` ficam disponíveis para consulta. Para executar com `df` e `acoes` já carregados, reexecute as células das etapas 2 e 3, as definições de funções, a chamada de Kruskal e a tabela de métricas, nessa ordem. A seção IPCA não é necessária nesse caminho. As saídas anteriores das células alteradas foram limpas para evitar confusão com a árvore antiga.

## Entrada de Kruskal e Prim

Os algoritmos recebem um DataFrame de distâncias de Mantegna quadrado, não vazio, numérico e simétrico. Linhas e colunas devem conter os mesmos ativos, sem duplicatas e na mesma ordem. Distâncias conhecidas devem estar entre 0 e 2; a diagonal conhecida deve ser zero. A comparação de simetria e diagonal usa tolerância absoluta de `1e-10`.

Valores `NaN` representam distâncias desconhecidas: as arestas correspondentes são ignoradas, sem preencher valores nem excluir ativos automaticamente. Infinitos e outras entradas inválidas geram `ValueError`. Se as arestas conhecidas não conectarem todos os ativos, ambos os algoritmos geram `ValueError` em vez de retornar uma árvore inválida. Prim aceita pesos iguais a 2.

Após alterar as definições, reexecute a célula de importação de NumPy/Pandas e as células de definição de `validar_matriz`/`criar_arestas`, `find`/`union`/`kruskal` e `prim`. A importação de bibliotecas pode ser executada separadamente da linha `%run` para evitar um novo download. Recalcule os resultados antes de interpretar saídas antigas do notebook.

## Métricas da árvore

Na última célula de `Algoritimos.ipynb`, `calcular_graus(adjacencia)` retorna um dicionário `{vertice: grau}`. `calcular_excentricidade(adjacencia)` retorna `{vertice: excentricidade}` sem modificar a adjacência: percorre a árvore por DFS a partir de cada vértice, soma os pesos ao longo do caminho único e toma a maior distância.

Essas funções recebem a adjacência da MST, com arestas registradas nos dois sentidos e tuplas `(peso, vizinho)`, conforme `criar_dicionario_adjacencia(mst)`. A excentricidade pressupõe uma árvore com pesos válidos; não é um cálculo de caminhos mínimos para grafos com ciclos. Uma entrada desconexa gera `ValueError`. Um vértice isolado representado por `{0: []}` tem grau e excentricidade zero; uma adjacência vazia retorna dicionários vazios. O construtor atual não recupera um vértice isolado a partir de uma lista de arestas vazia.

Para usar, reexecute a última célula e chame `adjacencia = criar_dicionario_adjacencia(mst_kruskal)`, `graus = calcular_graus(adjacencia)` e `excentricidades = calcular_excentricidade(adjacencia)`.

`distancia_entre_vertices(adjacencia, origem, destino)` retorna a soma dos pesos no caminho único entre os dois vértices, usando DFS. A distância de um vértice a ele mesmo é zero. Vértices inexistentes ou ausência de caminho geram `ValueError`.

`calcular_diametro(adjacencia)` retorna a maior excentricidade. `calcular_centro(adjacencia)` retorna uma lista dos vértices que minimizam a excentricidade, considerando diferenças de até `1e-10` como empate e preservando a ordem da adjacência. O centro é formado por vértices; não inclui pontos interiores das arestas. Ambas as funções reaproveitam `calcular_excentricidade`, rejeitam árvores vazias e propagam o erro de desconexão. Para `{0: []}`, o diâmetro é zero e o centro é `[0]`.

Após reexecutar a célula das métricas, consulte, por exemplo, `distancia_entre_vertices(adjacencia, 0, 1)`, `calcular_diametro(adjacencia)` e `calcular_centro(adjacencia)`, usando índices existentes na árvore. As funções pressupõem uma MST válida com pesos finitos e não negativos; não validam ciclos nem substituem um algoritmo de caminhos mínimos para grafos gerais.
