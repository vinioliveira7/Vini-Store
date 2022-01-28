from cadastro import *
from cliente import exibir_clientes, excluir_clientes, exibir_dados
from estrutura import *

cabecalho('VINI STORE')

while True:
    # CADASTRAR UM CLIENTE
    resposta = menu(['CADASTRAR CLIENTE',
                     'ADICIONAR ENDEREÇO A CLIENTE',
                     'EXIBIR DADOS DO CLIENTE',
                     'EXCLUIR DADOS DO CLIENTE',
                     'EXIBIR CLIENTES CADASTRADOS',
                     'SAIR'])

    if resposta == 1:
        cabecalho('NOVO CADASTRO')
        cadastro_cliente()

    # CADASTRAR UM ENDEREÇO
    elif resposta == 2:
        cabecalho('NOVO ENDEREÇO')
        cadastro_endereco()
    
    # MOSTRAR DADOS DO CLIENTE
    elif resposta == 3:
        cabecalho('DADOS DO CLIENTE')
        exibir_dados()
    
    # MOSTRAR CLIENTES CADASTRADOS
    elif resposta == 4:
        cabecalho('EXCLUIR CLIENTE')
        excluir_clientes()
    
    elif resposta == 5:
        cabecalho('CLIENTES CADASTRADOS')
        exibir_clientes()

    # SAIR DO SISTEMA
    elif resposta == 6:
        cabecalho('Saindo do Sistema... Bye!')
        break
    else:
        print('\033[31mERRO: por favor digite uma opção válida.\033[m')
