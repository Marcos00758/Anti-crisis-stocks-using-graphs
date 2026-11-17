"""Simulacao das carteiras (buy-and-hold), metricas de risco, controles e graficos.

Pressupoe os objetos produzidos por Algoritimos.ipynb:
df, acoes_elegiveis, mst_kruskal, matriz_mantegna_formacao,
carteira_periferica, carteira_central, parametros.
Nada aqui participa da selecao das acoes: so le precos a partir da data de entrada.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

DIAS_ANO = 252
CORES = {
    'A - Periferica': '#D55E00',
    'B - Central': '#0072B2',
    'C - Setorial': '#009E73',
    'Ibovespa': '#000000',
    'Universo EW': '#7F7F7F',
}


# ---------------------------------------------------------------- precos
def trajetorias_normalizadas(close, fim_formacao, fim_avaliacao):
    """Precos de cada acao divididos pelo preco de entrada (base 1).

    Entrada = ultimo fechamento <= fim da formacao (decisao so com dados ate ali).
    Acao sem preco apos uma data (suspensa/deslistada) fica com o ultimo preco
    valido, isto e, e liquidada a esse preco e o caixa rende zero.
    """
    close = close.sort_index()
    data_entrada = close.loc[:fim_formacao].index[-1]
    precos = close.loc[data_entrada:fim_avaliacao]
    entrada = precos.iloc[0]
    precos = precos.loc[:, entrada.notna() & (entrada > 0)]
    norm = precos.ffill() / precos.iloc[0]
    return norm, data_entrada


def valor_buy_and_hold(norm, tickers, pesos=None):
    """Valor da carteira (base 1) com pesos iniciais fixos, sem rebalancear."""
    tickers = list(tickers)
    if pesos is None:
        pesos = pd.Series(1 / len(tickers), index=tickers)
    return (norm[tickers] * pesos.reindex(tickers)).sum(axis=1)


def carregar_ibov(pasta, indice_ref):
    """Ibovespa em base 1 alinhado a indice_ref; None se indisponivel.

    Usa <pasta>/ibov.csv (data, Close) se existir; senao tenta yfinance (^BVSP) e salva.
    Atencao: o Ibovespa e indice de preco; as acoes (auto_adjust) incluem proventos.
    """
    arq = Path(pasta) / 'ibov.csv'
    if arq.exists():
        serie = pd.read_csv(arq, index_col=0, parse_dates=True).iloc[:, 0]
    else:
        try:
            import yfinance as yf
            d = yf.download('^BVSP', start=indice_ref[0] - pd.Timedelta(days=10),
                            end=indice_ref[-1] + pd.Timedelta(days=1),
                            auto_adjust=True, progress=False)
            serie = d['Close']
            serie = serie.iloc[:, 0] if isinstance(serie, pd.DataFrame) else serie
            serie = serie.dropna().rename('Close')
            if serie.empty:
                return None
            Path(pasta).mkdir(parents=True, exist_ok=True)
            serie.to_csv(arq)
        except Exception as erro:
            print('Ibovespa indisponivel:', erro)
            return None
    serie = serie.sort_index().reindex(indice_ref, method='ffill')
    if serie.isna().any():
        print('Ibovespa nao cobre todo o periodo; ignorado.')
        return None
    return serie / serie.iloc[0]


# --------------------------------------------------------------- janelas
def limites(indice, ini, fim, base_anterior=True):
    """Posicoes (i0, i1) da janela; i0 e a base (valor antes do 1o retorno)."""
    i1 = indice.searchsorted(pd.Timestamp(fim), side='right') - 1
    i0 = indice.searchsorted(pd.Timestamp(ini), side='left')
    if base_anterior:
        i0 = max(i0 - 1, 0)
    return i0, i1


def janela_crise(ref, ano):
    """Pico->vale da referencia (benchmark) dentro de `ano`. Descritiva: vale para todos."""
    r = ref.loc[:f'{ano}-12-31']
    vale = (r / r.cummax() - 1).idxmin()
    pico = r.loc[:vale].idxmax()
    return pico, vale


def definir_janelas(ref, inicio_avaliacao, fim_avaliacao, ano_crise):
    pico, vale = janela_crise(ref, ano_crise)
    janelas = {
        'Avaliacao completa': (inicio_avaliacao, fim_avaliacao, True),
        f'Ano {ano_crise}': (f'{ano_crise}-01-01', f'{ano_crise}-12-31', True),
        f'Crise ({pico:%d/%m/%Y} a {vale:%d/%m/%Y})': (pico, vale, False),
    }
    return janelas, (pico, vale)


# -------------------------------------------------------------- metricas
def metricas_janela(valores, janela, ref=None):
    ini, fim, ant = janela
    i0, i1 = limites(valores.index, ini, fim, ant)
    S = valores.iloc[i0:i1 + 1]
    r = S.pct_change().iloc[1:]
    tab = pd.DataFrame({
        'Retorno acumulado': S.iloc[-1] / S.iloc[0] - 1,
        'Volatilidade anualizada': r.std(ddof=1) * np.sqrt(DIAS_ANO),
        'Max drawdown': 1 - (S / S.cummax()).min(),
        'Pior retorno diario': r.min(),
    })
    if ref is not None:
        rr = r[ref]
        tab['Beta vs ref'] = r.apply(lambda x: x.cov(rr) / rr.var())
        tab['Correlacao vs ref'] = r.corrwith(rr)
    return tab


def tabela_metricas(valores, janelas, ref=None):
    partes = {nome: metricas_janela(valores, j, ref) for nome, j in janelas.items()}
    tab = pd.concat(partes, names=['Janela', 'Estrategia'])
    return tab


# ----------------------------------------------- carteiras aleatorias
def carteiras_aleatorias(norm, universo, q, janelas, n=2000, semente=12345):
    """n carteiras aleatorias de q acoes do universo, equiponderadas, buy-and-hold."""
    rng = np.random.default_rng(semente)
    X = norm[list(universo)].to_numpy()
    idx = np.stack([rng.choice(len(universo), q, replace=False) for _ in range(n)])
    V = X[:, idx].mean(axis=2)  # T x n
    saida = {}
    for nome, (ini, fim, ant) in janelas.items():
        i0, i1 = limites(norm.index, ini, fim, ant)
        S = V[i0:i1 + 1]
        r = S[1:] / S[:-1] - 1
        saida[nome] = pd.DataFrame({
            'Retorno acumulado': S[-1] / S[0] - 1,
            'Volatilidade anualizada': r.std(axis=0, ddof=1) * np.sqrt(DIAS_ANO),
            'Max drawdown': 1 - (S / np.maximum.accumulate(S, axis=0)).min(axis=0),
        })
    return saida


def posicao_nas_aleatorias(tab, alea, estrategias):
    """Fracao das carteiras aleatorias com MDD (ou vol.) <= o da estrategia.

    Valor baixo = estrategia entre as menos arriscadas; ~0,5 = indistinguivel do acaso.
    """
    linhas = []
    for janela, base in alea.items():
        for est in estrategias:
            linha = {'Janela': janela, 'Estrategia': est}
            for m in ['Max drawdown', 'Volatilidade anualizada']:
                linha[f'Prop. aleatorias com {m} <= estrategia'] = float(
                    (base[m] <= tab.loc[(janela, est), m]).mean())
            linhas.append(linha)
    return pd.DataFrame(linhas).set_index(['Janela', 'Estrategia'])


# ------------------------------------------------------------ composicao
def composicao(carteiras, liquidez=None):
    """Tabela longa: carteira, ticker, peso inicial (igual) e liquidez da formacao."""
    linhas = []
    for nome, tickers in carteiras.items():
        for t in tickers:
            linhas.append({'Carteira': nome, 'Ticker': t, 'Peso inicial': 1 / len(tickers),
                           'Liquidez mediana na formacao (R$/dia)':
                               None if liquidez is None else liquidez.get(t, np.nan)})
    return pd.DataFrame(linhas)


def liquidez_formacao(df, inicio, fim):
    if 'Volume' not in df.columns.get_level_values(0):
        return None
    fin = df['Close'] * df['Volume']
    return fin.loc[inicio:fim].median()

# --------------------------------------------------------------- graficos
def _nome(t):
    return t.replace('.SA', '')


def _sombra(ax, crise):
    if crise is not None:
        ax.axvspan(crise[0], crise[1], color='#999999', alpha=0.15, lw=0)


def fig_evolucao(valores, crise, caminho=None):
    fig, ax = plt.subplots(figsize=(10, 5))
    for c in valores.columns:
        ax.plot(valores.index, valores[c], label=c, color=CORES.get(c), lw=1.6)
    _sombra(ax, crise)
    ax.axhline(1, color='k', lw=0.6, ls=':')
    ax.set(title='Evolucao do valor (base 1, buy-and-hold, sem rebalancear)', ylabel='Valor')
    ax.legend(frameon=False)
    fig.tight_layout()
    if caminho:
        fig.savefig(caminho, dpi=200)
    return fig


def fig_drawdown(valores, crise, caminho=None):
    fig, ax = plt.subplots(figsize=(10, 4.5))
    for c in valores.columns:
        ax.plot(valores.index, 100 * (valores[c] / valores[c].cummax() - 1),
                label=c, color=CORES.get(c), lw=1.4)
    _sombra(ax, crise)
    ax.set(title='Drawdown desde o maximo anterior', ylabel='%')
    ax.legend(frameon=False)
    fig.tight_layout()
    if caminho:
        fig.savefig(caminho, dpi=200)
    return fig


def fig_metricas(tab, caminho=None):
    janelas = list(tab.index.get_level_values(0).unique())
    metricas = [('Max drawdown', 'Max drawdown (%)'),
                ('Volatilidade anualizada', 'Volatilidade anualizada (%)')]
    fig, axs = plt.subplots(len(metricas), len(janelas), figsize=(4.2 * len(janelas), 6),
                            sharey='row', squeeze=False)
    for j, jan in enumerate(janelas):
        sub = tab.loc[jan]
        for i, (m, rot) in enumerate(metricas):
            ax = axs[i, j]
            v = 100 * sub[m]
            ax.bar(range(len(v)), v.values, color=[CORES.get(e, '#BBBBBB') for e in v.index])
            ax.set_xticks(range(len(v)))
            ax.set_xticklabels([e.split(' - ')[0] for e in v.index], rotation=30, ha='right')
            for k, val in enumerate(v.values):
                ax.text(k, val, f'{val:.0f}', ha='center', va='bottom', fontsize=8)
            if i == 0:
                ax.set_title(jan, fontsize=9)
            if j == 0:
                ax.set_ylabel(rot)
    fig.tight_layout()
    if caminho:
        fig.savefig(caminho, dpi=200)
    return fig


def fig_aleatorias(alea, tab, janela, estrategias, caminho=None):
    metricas = ['Max drawdown', 'Volatilidade anualizada']
    fig, axs = plt.subplots(1, 2, figsize=(11, 4))
    for ax, m in zip(axs, metricas):
        ax.hist(100 * alea[janela][m], bins=40, color='#CCCCCC', edgecolor='white')
        for e in estrategias:
            ax.axvline(100 * tab.loc[(janela, e), m], color=CORES.get(e), lw=2, label=e)
        ax.set(title=f'{m}: carteiras aleatorias (n={len(alea[janela])})', xlabel='%')
    axs[0].legend(frameon=False, fontsize=8)
    fig.suptitle(janela, fontsize=10)
    fig.tight_layout()
    if caminho:
        fig.savefig(caminho, dpi=200)
    return fig


def fig_mst(mst, tickers, periferica, central, caminho=None):
    """MST com as carteiras A e B destacadas. mst = [(peso, i, j)], tickers na ordem da matriz."""
    G = nx.Graph()
    G.add_nodes_from(range(len(tickers)))
    G.add_weighted_edges_from([(i, j, w) for w, i, j in mst])
    pos = nx.kamada_kawai_layout(G, weight='weight')
    cor, rotulos = [], {}
    for v, t in enumerate(tickers):
        a, b = t in periferica, t in central
        cor.append('#7B3294' if a and b else '#D55E00' if a else '#0072B2' if b else '#DDDDDD')
        if a or b:
            rotulos[v] = _nome(t)
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#999999', width=0.8)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=cor,
                           node_size=[30 + 25 * G.degree(v) for v in G], linewidths=0)
    pos_rot = {v: (x, y + 0.04) for v, (x, y) in pos.items()}
    nx.draw_networkx_labels(G, pos_rot, labels=rotulos, font_size=8, ax=ax)
    ax.set_title('MST (Kruskal): laranja = periferica (A), azul = central (B), roxo = ambas')
    ax.axis('off')
    fig.tight_layout()
    if caminho:
        fig.savefig(caminho, dpi=200)
    return fig


# ----------------------------------------------------------------- resumo
def resumo(tab, pos, estrategias):
    """Resumo objetivo dos resultados"""
    for jan in tab.index.get_level_values(0).unique():
        sub = tab.loc[jan]
        print(f'\n== {jan}')
        print('Ordem por menor Max drawdown:',
              ' < '.join(f'{e.split(" - ")[0]} ({100 * v:.1f}%)'
                         for e, v in sub['Max drawdown'].sort_values().items()))
        if {'A - Periferica', 'B - Central'} <= set(estrategias):
            a, b = sub.loc['A - Periferica'], sub.loc['B - Central']
            print(f'A tem MDD menor que B: {a["Max drawdown"] < b["Max drawdown"]}; '
                  f'vol. menor que B: {a["Volatilidade anualizada"] < b["Volatilidade anualizada"]}')
        for e in estrategias:
            p = pos.loc[(jan, e)]
            print(f'{e}: {100 * p.iloc[0]:.0f}% das aleatorias tem MDD <= ao dela; '
                  f'{100 * p.iloc[1]:.0f}% tem vol. <= a dela')

def salvar(pasta, valores, tab, pos, comp):
    pasta = Path(pasta)
    (pasta / 'tables').mkdir(parents=True, exist_ok=True)
    (pasta / 'figures').mkdir(parents=True, exist_ok=True)
    valores.to_csv(pasta / 'tables' / 'portfolio_daily_values.csv')
    tab.to_csv(pasta / 'tables' / 'metrics.csv')
    pos.to_csv(pasta / 'tables' / 'posicao_aleatorias.csv')
    comp.to_csv(pasta / 'tables' / 'portfolios.csv', index=False)