import pandas as pd # Biblioteca de ciência de dados https://pandas.pydata.org/pandas-docs/stable/
import re # https://docs.python.org/3/library/re.html
import warnings # Biblioteca anti warning
warnings.filterwarnings('ignore') # ou warnings.filterwarnings(action='once')
from pandas_datareader import data as web # crawler
from datetime import date # biblioteca para ver data/mes/ano/dia
from datetime import datetime
from .bolsa import* # Nossa classe com objetos da bolsa de valores
from .tratamento import* # Nossa classe de tratar as ações

def checkCrawler(dataFrame):
    # Se o mercado não estiver aberto, pode-se acabar gerando uma linha repetida do dia anterior (padrão yahoo)
    if(dataFrame['Data'][len(dataFrame['Data'])-1] == dataFrame['Data'][len(dataFrame['Data'])-2]):
        dataFrame['Data'][len(dataFrame['Data'])-1] = str(date.today())
    return dataFrame

def crawler(nome, start, end, num):
    # web.DataReader é um crawler já pronto
    dataFrame = pd.DataFrame(web.DataReader(nome, data_source='yahoo', start=start, end=end))
    # reseta o index pois vem em formato de timestamp no index
    dataFrame.reset_index(inplace=True)
    # converte o timestamp em str
    dataFrame['Date'] = dataFrame['Date'].map(tratamento.converteTimeStamp)
    tratamento.tratamentoInicial(dataFrame)
    dataFrame = checkCrawler(dataFrame)
    if(num==1):
        dataFrame.drop(0, inplace=True) # Remove a primeira linha do dataFrame que vai ficar repetida na concatenação/update
    return dataFrame

def updateData(Acao):
    data_atual = str(date.today())
    ultima_data = Acao.dataFrame['Data'][len(Acao.dataFrame['Data'])-1]
    if(data_atual == ultima_data):
        return Acao.dataFrame
    else:
        novos_dados = crawler(Acao.nome,ultima_data,data_atual,1)
        Acao.dataFrame = pd.concat([Acao.dataFrame, novos_dados])
        Acao.dataFrame = Acao.dataFrame.reset_index()
        Acao.dataFrame = Acao.dataFrame.drop('index',axis=1)
        return Acao.dataFrame
    
def downloadAcao(nome):
    data_inicial = '1/1/2000' # Vamos começar a trabalhar com ações a partir de 2000 onde os dados são mais confiaveis
    data_atual = str(date.today())
    dataFrame = crawler(nome,data_inicial,data_atual,0)
    dataFrame.to_csv('stocks/'+str(nome),index=False) # Salva a ação em csv