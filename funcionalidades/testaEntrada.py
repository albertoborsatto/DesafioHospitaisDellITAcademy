# a função testa se o programa encontrou algum registro da entrada do usuário na tabela
def procuraTabela(lista):
    if(len(lista) == 0):
        return False
    else:
        return True

# a função testa se a string de entrada possui algum número ou é vazia
def testaEntrada(string):
    if(len(string) > 0 and (all(x.isalpha() or x.isspace() for x in string))):  
        return True
    else:
        print('\nPor favor, digite uma entrada válida.')
        return False


