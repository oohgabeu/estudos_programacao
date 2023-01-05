import pandas as pd

# dataframe por dict python

vendas = {
    'data': ['15/02/2021', '16/02/2021'],
    'valor': [500, 300],
    'produto': ['feijao', 'arroz'],
    'qtde': [50, 70]
}

tabela_vendas = pd.DataFrame(vendas)
tabela_vendas

# dataframe por uma base de dados

tabela_vendas = pd.read_excel('vendas.xlsx')
tabela_vendas

# primeira visão da tabela

tabela_vendas.head(10)

# descrição estatística básica geral

tabela_vendas.describe()

# selecionando uma única coluna

produtos = tabela_vendas['Produto']
produtos

# selecionando várias colunas

tabela_selecionada = tabela_vendas[
    ['Produto', 'Valor Unitário']
]
tabela_selecionada.head()

# pegando linhas da tabela

tabela_selecionada.loc[1:10]

# pegando linhas por condição

tabela_selecionada.loc[
    tabela_selecionada['Valor Unitário'] > 200
].head()

# juntando filtros anteriores

select = tabela_vendas.loc[
    tabela_vendas['Valor Unitário'] > 200,
    ['Produto', 'Valor Unitário']
]

select.head()

# adicionando uma nova coluna 01

tabela_vendas['Comissão'] = tabela_vendas['Valor Final'] * 0.05
tabela_vendas.head()

# adicionando uma nova coluna 02

tabela_vendas.loc[:, 'Comissão'] = tabela_vendas['Valor Final'] * 0.07
tabela_vendas.head()

# deletando colunas

tabela_vendas = tabela_vendas.drop('Comissão', axis=1)
tabela_vendas

# deletando linhas

tabela_vendas = tabela_vendas.drop(0, axis=0)
tabela_vendas
