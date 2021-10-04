from funcionalidades.testaEntrada import procuraTabela, testaEntrada


def infInternacao(df):
    while True:
        mun = input('Informe o nome do seu município: ').upper()
        if(testaEntrada(mun)): 
            break
    
    anos = internacoesAno(df, mun)
    testaImpressao(anos, mun)
    
    
def internacoesAno(df, mun):
    cidade = df.loc[df['municipio_residencia'] == mun, :] # filtra a tabela a partir da cidade informada
    
    if(procuraTabela(cidade)):
        # filtra a tabela por intervalo de datas de internção e armazena em variáveis para cada ano
        dezoito = cidade.loc[(cidade['data_internacao'] >= '2018-01-01') & (cidade['data_internacao'] <= '2018-12-31')]
        dezenove = cidade.loc[(cidade['data_internacao'] >= '2019-01-01') & (cidade['data_internacao'] <= '2019-12-31')]
        vinte = cidade.loc[(cidade['data_internacao'] >= '2020-01-01') & (cidade['data_internacao'] <= '2020-12-31')]
        vinteeum = cidade.loc[(cidade['data_internacao'] >= '2021-01-01') & (cidade['data_internacao'] <= '2021-12-31')]

        return [dezoito, dezenove, vinte, vinteeum]
    else:
        return 0


# a função testa se dever imprimir as informações ou a mensagem de erro
def testaImpressao(anos, mun):
    if(anos): # se anos == 0, isso mostra a função de teste encontrou registros do município na tabela
        mostraInfos(anos, mun)
    else:  
        print(f'\nNenhuma cidade com o nome {mun} encontrada na tabela.')
    

def mostraInfos(anos, mun):
    print(f'\nNúmero de internações em {mun} por ano entre 2018 e 2021:\n')
    print(f'Internações em 2018: {len(anos[0])}')
    print(f'Internações em 2019: {len(anos[1])}')
    print(f'Internações em 2020: {len(anos[2])}')  # o tamanho de cada posição do vetor representa o número de internações em cada ano
    print(f'Internações em 2021: {len(anos[3])}')
    