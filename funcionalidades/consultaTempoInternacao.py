from funcionalidades.consultaInternacao import mostraInfos
import os
import pandas as pd
from funcionalidades.testaEntrada import procuraTabela, testaEntrada


def infTempoInternacao(df):
    while True:
        solic = input('Informe o nome do solicitante: ').upper()
        if(testaEntrada(solic)): # testa se o usuário digitou algo ou deu uma entrada com números
            break
        
    final = listaPacientes(df, solic)
    if(isinstance(final, pd.DataFrame)): # testa se o retorno da função é um objeto, para checar se é uma tabela
        return final
    else:
        return f'\nNenhum solicitante com o nome {solic} encontrado.'
    

def listaPacientes(df, solic):
    colunas = ['id_usuario', 'sexo', 'idade', 'municipio_residencia', 
               'solicitante', 'executante', 'data_solicitacao', 'data_alta']

    pacientes = df.loc[df['solicitante'] == solic, colunas]

    # passa as colunas para o formato datetime, cria uma nova coluna que armazena a subtração entre as datas passada para dias
    pacientes['data_solicitacao'] = pd.to_datetime(pacientes.data_solicitacao) 
    pacientes['data_alta'] = pd.to_datetime(pacientes.data_alta)
    pacientes['tempo_internacao'] = pacientes['data_alta'] - pacientes['data_solicitacao']
    colunas = atualizaColunas(colunas)

    if(procuraTabela(pacientes)): 
        pacientes = trataNaT(pacientes)
        return pacientes.loc[:, colunas]
    else:
        return 0
        
        
# a função substitui as posições vazias da coluna 'tempo_internanção' pela string 'AINDA INTERNADA'
def trataNaT(pacientes):
    pacientes['tempo_internacao'] = (pacientes['tempo_internacao'].astype(str)
                                    .replace({'NaT': 'AINDA INTERNADA'}))
    return pacientes


#atualiza as colunas desejadas para a impressão da tabela
def atualizaColunas(colunas):
    del colunas[6:8]
    colunas.append('tempo_internacao')
    
    return colunas  


    




    
    
