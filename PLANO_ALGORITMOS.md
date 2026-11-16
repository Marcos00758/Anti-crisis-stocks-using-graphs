# Plano: algoritmos e seleção de carteiras

## Responsabilidades e entrega

Esta parte do trabalho abrange a construção da MST com Kruskal e Prim, os pesos das arestas, os graus dos vértices, as métricas estruturais e as regras de escolha dos ativos. Grau é uma propriedade dos vértices; peso é uma propriedade das arestas.

Simulação das carteiras, benchmarks, métricas de risco, análise dos resultados financeiros e visualizações gráficas são responsabilidade de outro integrante. Não será criado um notebook de backtesting nesta parte.

O estudo inicial usa a formação de 01/01/2017 a 31/12/2019. A avaliação financeira de 01/01/2020 a 31/12/2022 será informada ao outro integrante; seus retornos não participam da seleção. O estudo da crise de 2008 fica para depois.

## Etapa 1 — Configuração e preservação da entrada

Situação: código implementado; a coleta local ainda depende da execução do notebook.

- `parametros_experimento.json` centraliza os períodos e a pasta da coleta.
- Ambos os notebooks têm uma célula inicial identificada como etapa 1. Ela mostra os parâmetros e a situação da pasta local, sem executar downloads.
- `baixar_acoes` inicia uma lista de lotes nova a cada chamada.
- A célula de coleta de `Tabelas_Acoes.ipynb` grava `acoes.csv` e `metadados.json` na primeira coleta e reutiliza esses arquivos nas seguintes. Os metadados registram origem, horário UTC, parâmetros, tickers, versões e hash do CSV.
- A cópia não é sobrescrita automaticamente. A entrada financeira fornecida pelo grupo pode substituir uma nova coleta, desde que sua origem e seu formato sejam registrados; não se deve atribuir a ela uma data de download inventada.

Arquivos envolvidos: `parametros_experimento.json`, `Tabelas_Acoes.ipynb`, `Algoritimos.ipynb` e documentação. A coleta integral pode conter outros períodos; isso não autoriza usá-los na formação.

Conferência manual: executar apenas a célula inicial de parâmetros deve mostrar as datas sem downloads. Executar as células de dados cria a cópia, caso ela não exista, ou verifica e carrega a cópia existente. Não executar a coleta apenas para conferir as datas.

## Etapa 2 — Preparar a entrada da formação

Situação: planejada, ainda não implementada.

Em `Algoritimos.ipynb`, separar os retornos de fechamento de 2017–2019 e definir os ativos elegíveis. Preservar a base original. A elegibilidade deve usar apenas informações anteriores ao período de avaliação.

Regras propostas, a fixar antes da avaliação:

- A ação já estar negociada no início da formação. A fundação da empresa não basta. O primeiro preço da fonte não comprova, sozinho, a data de listagem; mudanças de ticker devem ser documentadas.
- Ter pelo menos 90% dos retornos esperados na janela, usando um calendário de sessões definido com o integrante que prepara os dados.
- Ter retornos com variância positiva. Preços não positivos e falhas da fonte devem ser investigados.
- Gerar uma tabela por ticker com cobertura, variância, situação e motivo de exclusão ou pendência. Não excluir automaticamente uma ação por qualquer lacuna ou pelo desempenho posterior.

A fonte atual consulta o universo disponível hoje. Recuperar ou receber do grupo o universo histórico é necessário para tratar o viés de sobrevivência; se não for possível, a limitação deve acompanhar a entrega.

Entrega intermediária: tabela de elegibilidade e retornos da formação. A exclusão manual de `RENT4.SA` deverá dar lugar à regra geral documentada.

## Etapa 3 — Construir a matriz de entrada do grafo

Situação: planejada, reaproveitando Pearson e Mantegna existentes.

Calcular Pearson somente sobre os retornos da formação dos ativos elegíveis. Proposta: exigir, por par, observações conjuntas equivalentes a pelo menos 80% das sessões da formação. Investigar a viabilidade de uma amostra comum de datas; pares com datas diferentes limitam a interpretação geométrica de Mantegna.

Aplicar Mantegna e conferir rótulos, simetria, diagonal, pesos finitos conhecidos e intervalo de 0 a 2. Não inventar correlações, preencher distâncias desconhecidas nem forçar conectividade. Havendo desconexão, registrar componentes e investigar a entrada antes de decidir uma restrição adicional do universo.

Entrega intermediária: matriz da formação e correspondência estável entre índice do vértice e ticker.

## Etapa 4 — Construir e conferir a MST

Situação: Kruskal e Prim já existem; falta aplicá-los à nova entrada.

Preservar a lógica atual. Conferir número de arestas `n-1`, ausência de ciclos, conectividade, pesos válidos e concordância do peso total entre os algoritmos, com tolerância numérica. Empates podem produzir árvores diferentes com o mesmo peso mínimo; é preciso fixar a árvore utilizada nas etapas seguintes, inicialmente a de Kruskal com desempate por índices derivados dos tickers ordenados.

Não criar uma suíte de testes nem adicionar NetworkX nesta etapa sem solicitação. As conferências serão apresentadas em saídas simples do notebook.

## Etapa 5 — Calcular as métricas estruturais

Situação: as funções já existem; falta usá-las na MST de 2017–2019.

Reaproveitar a adjacência não dirigida com tuplas `(peso, vizinho)`, `calcular_graus`, `calcular_excentricidade`, `distancia_entre_vertices`, `calcular_diametro` e `calcular_centro`.

Montar uma tabela com ticker, índice, grau, excentricidade ponderada e identificação de folha e centro. A excentricidade soma os pesos ao longo dos caminhos da árvore, sem representar uma medida financeira de risco.

## Etapa 6 — Fixar e implementar as regras de seleção

Situação: planejada, ainda não implementada.

Regra inicial proposta: oito menores excentricidades para a carteira central e oito maiores para a periférica. Desempatar por ticker em ordem alfabética; verificar universo mínimo, empates e possível sobreposição. Se houver sobreposição, a regra para resolvê-la deve ser definida antes da avaliação, sem exclusões silenciosas.

Usar o grau como informação estrutural; não misturá-lo ao ranking sem uma regra explícita. Distinguir os oito vértices do ranking periférico da periferia matemática estrita, formada pelos vértices de excentricidade máxima.

Entrega intermediária: listas de ativos e explicação reproduzível de cada seleção. Nenhum retorno de 2020–2022 será usado para escolher ou ajustar as regras.

## Etapa 7 — Exportar para o integrante da avaliação

Situação: planejada, ainda não implementada.

Exportar CSVs com a tabela de elegibilidade, as arestas da MST e as métricas/seleções. Incluir tickers, graus, excentricidades, estratégia, posição no ranking, datas de formação e identificação da base de entrada. Registrar as regras e os desempates. Pesos financeiros iniciais só serão incluídos se combinados com o responsável pela simulação.

A entrega termina nesses arquivos e em instruções de leitura. O outro integrante decide e implementa execução de compras, rebalanceamento, custos, eventos corporativos durante a avaliação, benchmarks, métricas financeiras e gráficos.

## Forma de trabalho

Avançar uma etapa de cada vez, explicar os arquivos e as regras afetadas e apresentar a saída intermediária antes da próxima alteração. Preservar funções e alterações do usuário. Não executar novos downloads para gerar resultados experimentais sem necessidade. Não fazer commit ou push sem solicitação.
