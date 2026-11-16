# Plano: algoritmos e seleção de carteiras

## Responsabilidades e entrega

Esta parte do trabalho abrange a construção da MST com Kruskal e Prim, os pesos das arestas, os graus dos vértices, as métricas estruturais e as regras de escolha dos ativos. Grau é uma propriedade dos vértices; peso é uma propriedade das arestas.

Simulação das carteiras, benchmarks, métricas de risco, análise dos resultados financeiros e visualizações gráficas são responsabilidade de outro integrante. Não será criado um notebook de backtesting nesta parte.

O estudo inicial usa a formação de 01/01/2017 a 31/12/2019. A avaliação financeira de 01/01/2020 a 31/12/2022 será informada ao outro integrante; seus retornos não participam da seleção. O estudo da crise de 2008 fica para depois.

## Etapa 1 — Configuração e preservação da entrada

Situação: código implementado e coleta local disponível em `dados/pandemia`.

- `parametros_experimento.json` centraliza os períodos e a pasta da coleta.
- Ambos os notebooks têm uma célula inicial identificada como etapa 1. Ela mostra os parâmetros e a situação da pasta local, sem executar downloads.
- `baixar_acoes` inicia uma lista de lotes nova a cada chamada.
- A célula de coleta de `Tabelas_Acoes.ipynb` grava `acoes.csv` e `metadados.json` na primeira coleta e reutiliza esses arquivos nas seguintes. Os metadados registram origem, horário UTC, parâmetros, tickers, versões e hash do CSV.
- A cópia não é sobrescrita automaticamente. A entrada financeira fornecida pelo grupo pode substituir uma nova coleta, desde que sua origem e seu formato sejam registrados; não se deve atribuir a ela uma data de download inventada.

Arquivos envolvidos: `parametros_experimento.json`, `Tabelas_Acoes.ipynb`, `Algoritimos.ipynb` e documentação. A coleta integral pode conter outros períodos; isso não autoriza usá-los na formação.

Conferência manual: executar apenas a célula inicial de parâmetros deve mostrar as datas sem downloads. Executar as células de dados cria a cópia, caso ela não exista, ou verifica e carrega a cópia existente. Não executar a coleta apenas para conferir as datas.

## Etapa 2 — Preparar a entrada da formação

Situação: código implementado em `Algoritimos.ipynb` e executado com a coleta local. A revisão dos motivos de exclusão e pendência continua necessária antes da seleção definitiva.

As células da seção **Etapa 2 - Elegibilidade e retornos da formacao (2017-2019)** preparam os retornos de fechamento e a tabela de elegibilidade. A base original é preservada. Os preços são limitados ao fim da formação antes dos cálculos; o fechamento anterior ao início pode ser usado para calcular o primeiro retorno de 2017. Não são usados dados da avaliação.

Regras implementadas:

- Cobertura de pelo menos 90%, definida por `cobertura_minima_formacao` em `parametros_experimento.json`, pelo menos dois retornos e variância positiva e finita. Descumprir esses critérios gera `Excluida`.
- Conforme escolha do usuário, as datas presentes na base são a referência provisória de sessões. A função aceita um calendário pelo argumento `sessoes`; a base não permite recuperar uma sessão ausente de todos os ativos. A cobertura não equivale a uma conferência oficial do calendário da B3.
- Exigir evidência de preço positivo e finito até a primeira sessão da formação e preço positivo e finito na última sessão de referência. A falta dessa evidência gera `Pendente`, salvo se já houver um motivo numérico de exclusão. A fundação da empresa e a data do IPO não são inferidas desses dados; mudanças de ticker devem ser verificadas.
- Preços não positivos ou infinitos na formação são contabilizados, desconsiderados no cálculo dos retornos e sinalizados para investigação. Se os critérios numéricos forem atendidos, a situação é `Pendente`, em vez de inclusão silenciosa. Não preencher lacunas.
- `Elegivel` significa elegibilidade pelos dados observáveis, não certificação da listagem histórica. Gerar uma linha por ticker, incluindo os solicitados sem fechamento disponível, com datas, cobertura, variância, preços inválidos, situação e motivos.

Saídas em memória: `tabela_elegibilidade`, `retornos_formacao` (todos os tickers), `acoes_elegiveis` (ordenadas por ticker) e `retornos_formacao_elegiveis`. Pendências não entram na lista de elegíveis. Os retornos são logarítmicos, calculados apenas a partir de fechamentos positivos e finitos; os pesos de outras colunas e o IPCA não participam desta etapa. A exportação continua prevista na etapa 7.

A fonte atual consulta o universo disponível hoje. Recuperar ou receber do grupo o universo histórico é necessário para tratar o viés de sobrevivência; se não for possível, a limitação deve acompanhar a entrega.

Conferência manual: com `df` e `acoes` já carregados e NumPy/Pandas importados, executar as células de definição e uso de `preparar_formacao`. Conferir a contagem por situação e investigar as linhas excluídas ou pendentes. Não é necessário repetir o `%run` apenas para executar a etapa 2. O fluxo das etapas 2–5 foi executado com o CSV local, sem novos downloads e sem chamar Prim; essa execução não grava as saídas no arquivo do notebook, que devem ser recalculadas no editor.

Integração realizada: Pearson e Mantegna recebem `retornos_formacao_elegiveis`. A exclusão manual de `RENT4.SA` foi retirada; a regra geral de elegibilidade determina os ativos da entrada. Reexecutar as células antes de interpretar os resultados da formação.

## Etapa 3 — Construir a matriz de entrada do grafo

Situação: implementada, reaproveitando Pearson e Mantegna existentes.

Pearson usa somente `retornos_formacao_elegiveis`. O mínimo por par é `ceil(numero_de_datas * proporcao_minima_observacoes_conjuntas)`, configurado como 80% no JSON. São geradas `matriz_correlacoes_formacao` e `matriz_mantegna_formacao`. O cálculo continua por pares de observações disponíveis; datas diferentes entre pares limitam a interpretação geométrica de Mantegna.

As validações existentes são preservadas, sem acrescentar validações ou testes, conforme solicitado. Não são inventadas correlações, preenchidas distâncias desconhecidas ou forçada conectividade. Se a validação existente acusar desconexão, investigar a entrada antes de decidir uma restrição adicional do universo. A ramificação IPCA continua exploratória e não alimenta esta MST.

Entrega intermediária: matriz da formação e correspondência estável entre índice do vértice e ticker.

## Etapa 4 — Construir e conferir a MST

Situação: Kruskal integrado à matriz da formação. Prim permanece definido, mas sua chamada e seus resultados continuam comentados por solicitação do usuário.

Os algoritmos existentes não foram reescritos. `mst_kruskal` usa `matriz_mantegna_formacao`; a saída mantém quantidade de arestas e peso total. Os índices derivam dos tickers ordenados na etapa 2, preservando o desempate atual de Kruskal. Nenhuma comparação com Prim é executada nesta versão.

Não foram acrescentadas validações, testes ou NetworkX. As verificações já existentes nas funções foram mantidas.

## Etapa 5 — Calcular as métricas estruturais

Situação: funções existentes integradas à MST de 2017–2019.

Reaproveitar a adjacência não dirigida com tuplas `(peso, vizinho)`, `calcular_graus`, `calcular_excentricidade`, `distancia_entre_vertices`, `calcular_diametro` e `calcular_centro`.

A tabela `metricas` contém `Vertice`, `Ticker`, `Grau`, `Excentricidade`, `Folha` e `Centro`. Os tickers são recuperados das colunas de `matriz_mantegna_formacao`, com os mesmos índices usados por Kruskal. As variáveis `diametro` e `centro` guardam os resultados correspondentes. A excentricidade soma os pesos ao longo dos caminhos da árvore, sem representar uma medida financeira de risco.

## Etapa 6 — Fixar e implementar as regras de seleção

Situação: duas células de seleção implementadas no final de `Algoritimos.ipynb`, após a tabela `metricas`.

`carteira_central` seleciona as oito menores excentricidades; `carteira_periferica`, as oito maiores. Ambas desempatam por ticker em ordem alfabética, preservam as colunas de `metricas` e exibem as seleções sem alterar a tabela original. Executar primeiro a célula que cria `metricas` e depois cada célula de carteira. Não foram acrescentados testes ou validações.

As seleções são independentes: não se remove eventual sobreposição automaticamente. Se ela ocorrer, a regra para resolvê-la precisa ser definida antes da avaliação. Se o universo contiver menos de oito ações, a seleção retorna as disponíveis; essa implementação simples não gera erro adicional.

Usar o grau como informação estrutural; não misturá-lo ao ranking sem uma regra explícita. Distinguir os oito vértices do ranking periférico da periferia matemática estrita, formada pelos vértices de excentricidade máxima.

Entrega intermediária: listas de ativos e explicação reproduzível de cada seleção. Nenhum retorno de 2020–2022 será usado para escolher ou ajustar as regras.

## Etapa 7 — Exportar para o integrante da avaliação

Situação: planejada, ainda não implementada.

Exportar CSVs com a tabela de elegibilidade, as arestas da MST e as métricas/seleções. Incluir tickers, graus, excentricidades, estratégia, posição no ranking, datas de formação e identificação da base de entrada. Registrar as regras e os desempates. Pesos financeiros iniciais só serão incluídos se combinados com o responsável pela simulação.

A entrega termina nesses arquivos e em instruções de leitura. O outro integrante decide e implementa execução de compras, rebalanceamento, custos, eventos corporativos durante a avaliação, benchmarks, métricas financeiras e gráficos.

## Forma de trabalho

Avançar uma etapa de cada vez, explicar os arquivos e as regras afetadas e apresentar a saída intermediária antes da próxima alteração. Preservar funções e alterações do usuário. Não executar novos downloads para gerar resultados experimentais sem necessidade. Não fazer commit ou push sem solicitação.
