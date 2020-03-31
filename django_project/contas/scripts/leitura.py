import os
import pandas as pd # Biblioteca de ciência de dados https://pandas.pydata.org/pandas-docs/stable/
import bolsa # Nossa classe com objetos da bolsa de valores
import mineracao # Nossa classe de minerar dados

def leituraDados():
    
    dados = list()
    lista_arq = os.listdir('stocks') # lista os arquivos no diretório de stocks
    
    if(lista_arq[0] == '.ipynb_checkpoints'): # anti-bug do jupyter
        for i in range(1,len(lista_arq)):
            DataFrame = pd.read_csv('stocks/'+str(lista_arq[i])) # transforma todos arquivos em dataFrame
            dados.append(bolsa.Acao(lista_arq[i],DataFrame)) # transforma todos dataFrames em ações
    else:
        for i in range(0,len(lista_arq)):
            DataFrame = pd.read_csv('stocks/'+str(lista_arq[i]))
            dados.append(bolsa.Acao(lista_arq[i],DataFrame))
            
    for i in range(0,len(dados)):
        mineracao.updateData(dados[i])

    return bolsa.BancoDeDados(dados)