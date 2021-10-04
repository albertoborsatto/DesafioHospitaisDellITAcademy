import pandas as pd
from funcionalidades.testaEntrada import procuraTabela, testaEntrada


def infHospitais(df):
    while True:
        exec = input('Informe o nome do executante: ').upper()
        if(testaEntrada(exec)): # testa se o usuário digitou algo ou deu uma entrada com números
            break
    
    final = informaDados(df, exec)
    if (isinstance(final, pd.DataFrame)):
        return final
    else:
        return f'\nNenhum executante com o nome {exec} econtrado.'

    
def informaDados(df, exec):
    colunas = ['idade', 'municipio_residencia', 'solicitante', 'executante', 'data_autorizacao',
                'data_internacao', 'data_alta']

    dados = df.loc[df['executante'] == exec, :] # filtra a tabela a partir do executante informado
    if(procuraTabela(dados)): 
        return dados.loc[:, colunas] # retorna todas as linhas e apenas as colunas informadas da tabela
    else:
        return 0
    

