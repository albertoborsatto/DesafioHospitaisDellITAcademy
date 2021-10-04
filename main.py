import pandas as pd
import os
from Menu.menu import menu
from funcionalidades.consultaMediaIdade import infMedias
from funcionalidades.consultaInternacao import infInternacao
from funcionalidades.consultaHospitais import infHospitais
from funcionalidades.consultaTempoInternacao import infTempoInternacao
from funcionalidades.consultaEsperaFila import esperaFila


try:
    df = pd.read_csv('./Tabela/gerint_solicitacoes_mod.csv', delimiter=';') # le o arquivo .csv e atribui uma variável para conter a tabela lida
    pd.set_option('display.max_rows', None) # comando para todas as linhas da tabela serem imprimidas 
except:
    print('Erro na leitura da tabela. Programa encerrando...\n')
    exit() 


# enquanto a entrada for diferente de 6, o programa continua executando
while True:
    op = menu()
    if(op == 1):
        infMedias(df)
    elif(op == 2):
        infInternacao(df)
    elif(op == 3):
        print(infHospitais(df))
    elif(op == 4):
        print(infTempoInternacao(df))
    elif(op == 5):
        cinco_mais = esperaFila(df)
        print('\nOs cinco casos com maior tempo de espera na fila:\n')
        print(cinco_mais)
    elif(op == 6):
        os.system('clear') or None
        print('Programa encerrado...')
        break

