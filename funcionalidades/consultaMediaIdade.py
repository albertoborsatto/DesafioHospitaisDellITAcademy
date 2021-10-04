import math
from funcionalidades.testaEntrada import testaEntrada, procuraTabela


def infMedias(df):
    while True:
        mun = input('Informe o nome do seu município: ').upper() 
        if(testaEntrada(mun)): # testa se a entrada do usuário é válida
            break
    
    medias = mediaIdades(mun, df)
    pacientes = totalPacientes(mun, df)
    testaImpressao(medias, pacientes, mun)
    

def mediaIdades(mun, df):
    cidade = df.loc[df['municipio_residencia'] == mun, :] # filtra a tabela a partir da cidade informada
    
    if(procuraTabela(cidade)): # testa se a tabela é vazia ou não
        todos = cidade['idade']
        mulheres = cidade.loc[cidade['sexo'] == 'FEMININO', 'idade']
        homens = cidade.loc[cidade['sexo'] == 'MASCULINO', 'idade'] #filtra a coluna de idade por gênero informado e armazena em variáveis separadas
        nInformado = cidade.loc[cidade['sexo'] == 'NÃO INFORMADO', 'idade']
    
        mediaM = mulheres.mean()
        mediaH = homens.mean()  # a função mean() calcula a média dos valores das colunas da tabela
        mediaT = todos.mean()
        mediaN = nInformado.mean()
        
        return testaMedias(mediaT, mediaM, mediaH, mediaN)
    else:
        return 0


def totalPacientes(mun, df):
    lista_mun = list(filter(lambda x: x == mun, df['municipio_residencia'])) # filtra os pacientes pelo município informado e os coloca num vetor
    numPacientes = len(lista_mun) # o tamanho desse vetor representará o número de pacientes da cidade
    return numPacientes


# a função checa se alguma média é 'NaN', caso for, troca o valor para 0
def testaMedias(mediaT, mediaM, mediaH, mediaN):
    medias = [mediaT, mediaM, mediaH, mediaN]
    
    for i in range(len(medias)):
        if(math.isnan(medias[i])): 
            medias[i] = 0

    return medias


# a função testa se dever imprimir as informações ou a mensagem de erro
def testaImpressao(medias, pacientes, mun):
    if(medias != 0): # se medias != 0, isso mostra a função de teste encontrou registros do município na tabela
        mostraInfos(pacientes, medias, mun)
    else:  
        print(f'\nNenhuma cidade com o nome {mun} encontrada na tabela.')


def mostraInfos(total, medias, mun):
    print(f'\nNúmero total de pacientes em {mun}: {total}')
    print(f'Média de idade das mulheres: {medias[1]:.2f} anos')
    print(f'Média de idade dos homens: {medias[2]:.2f} anos')
    print(f'Média de idade dos pacientes com  o sexo não informado: {medias[3]:.2f} anos')
    print(f'Média de idade de todos os pacientes: {medias[0]:.2f} anos')