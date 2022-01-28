from cadastro import *
from estrutura import cabecalho


def exibir_dados():
    login = input('Login: ')
    senha = input('Senha: ')

    try:
        cliente = clientes[login]
        if senha != cliente[2]:
            print('=> \033[31mSenha incorreta\033[m')
            return
    except:
        print('=> \033[33mCliente não cadastrado\033[m')
        return

    cabecalho('INFORMAÇÕES DO CLIENTE')
    print(f'=> Nome: {cliente[0]}')
    print(f'=> Login: {cliente[1]}')
    print(f'=> Senha: {cliente[2]}')
    print(f'=> Email: {cliente[3]}')
    print(f'=> Telefone: {cliente[4]}')
    print(f'=> Data de nascimento: {cliente[5]}')
        
    # SE O CLIENTE JA TIVER CADASTRADO UM ENDEREÇO
    if len(cliente) > 6:

        cabecalho('ENDEREÇO(S) DO CLIENTE')
        cont = 6
        while cont < len(cliente):
            cabecalho(f'ENDEREÇO {cont-5}')
            print(f'=> Rua: {cliente[cont][0]}')
            print(f'=> Número: {cliente[cont][1]}')
            print(f'=> Complemento: {cliente[cont][2]}')
            print(f'=> Bairro: {cliente[cont][3]}')
            print(f'=> Cidade: {cliente[cont][4]}')
            print(f'=> CEP: {cliente[cont][5]}')
            print(f'=> Ponto de referência: {cliente[cont][6]}')
            cont += 1


def exibir_clientes():
    if len(clientes) == 0:
        cabecalho('NENHUM CLIENTE CADASTRADO!')
    for key, value in clientes.items():
        print(f'=> Login: {key}\n   Nome: {value[0]}')


def excluir_clientes():
    login = input('Login: ')
    senha = input('Senha: ')

    try:
        cliente = clientes[login]
        if senha != cliente[2]:
            print('=> \033[31mSenha incorreta\033[m')
            return
    except:
        print('=> \033[33mUsuário não cadastrado\033[m')
        return

    resposta = input('Deseja realmente excluir esse cliente? [S/N] ').strip().upper()[0]
    while resposta not in 'NnSs':
        print('\033[31mERRO! ESCOLHA UM OPÇÃO VÁLIDA!\033[m')
        resposta = input('Deseja realmente excluir esse cliente? [S/N] ').strip().upper()[0]

    if resposta in 'S':
        cabecalho(f'Cliente foi excluido!')
        del clientes[login]
