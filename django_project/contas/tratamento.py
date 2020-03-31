import pandas as pd # Biblioteca de ciência de dados https://pandas.pydata.org/pandas-docs/stable/
from datetime import date # biblioteca para ver data/mes/ano/dia

def descobreAno(data):
    return data[0:4]

def descobreMes(data):
    return data[5:7]
    
def tratamentoInicial(dataFrame):
    # Renomeia as colunas em inglês
    dataFrame.rename(columns={'Date': 'Data',
                              'Open': 'Abertura', 
                              'High': 'Máxima', 
                              'Low': 'Mínima', 
                              'Close' : 'Fechamento', 
                              'Adj Close': 'Fechamento Ajustado'}, inplace=True)
    # Remove dados vazios
    dataFrame.dropna(axis=0, how='any', inplace=True)
    # Colunas auxiliares para as bandas de boolinger
    dataFrame['30 Day MA'] = dataFrame['Fechamento Ajustado'].rolling(window=20).mean()
    dataFrame['30 Day STD'] = dataFrame['Fechamento Ajustado'].rolling(window=20).std()
    dataFrame['Upper Band'] = dataFrame['30 Day MA'] + (dataFrame['30 Day STD'] * 2)
    dataFrame['Lower Band'] = dataFrame['30 Day MA'] - (dataFrame['30 Day STD'] * 2)
    # Cria os meses e ano das ações através da função de mapeamento
    dataFrame['Mês'] = dataFrame['Data'].map(descobreMes)
    dataFrame['Ano'] = dataFrame['Data'].map(descobreAno)

    return dataFrame

def converteTimeStamp(data):
    return data.strftime("%Y-%m-%d")