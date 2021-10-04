import os
from funcionalidades.testaEntrada import procuraTabela

def esperaFila(df):
    # a função sort_values realiza o ordenamento de uma coluna específica da tabela, nesse caso em ordem descrescente
    df.sort_values(by=['horas_na_fila'], inplace=True, ascending=False) 
    
    return df.iloc[0:5] # a função iloc está filtrando a tabela da linha 0 até a 4
    

    