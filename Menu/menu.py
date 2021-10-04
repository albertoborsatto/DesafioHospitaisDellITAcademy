import os

def menu():
    print('\n\n===  MENU  ===')
    print('1. Consultar média de idade dos pacientes')
    print('2. Consultar internações por ano')
    print('3. Consultar hospitais')
    print('4. Calcular tempo de internação')
    print('5. Determinar tempos de espera na fila')
    print('6. Terminar o programa')
    
    #caso a entrada do usuário não seja um inteiro dentro do intervalo [1, 6], 
    # a entrada não é aceita e a mensagem de erro é mostrada
    while True:
        try:
            op = int(input('\nEscolha uma das opções: '))
            if op not in range(1, 7):
                raise ValueError   
            break
        except ValueError:  
            print('Por favor, digite um número dentro do intervalo [1, 6]')
    
    return int(op)