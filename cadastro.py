from estrutura import *


clientes = dict()


def cadastro_cliente():
    while True:
        nome = input('Nome Completo: ')
        
        login = input('Login: ')
        while login in clientes.keys():
            print('LOGIN JÁ EXISTE!')
            login = input('login: ')

        senha = input('Senha: ')
        
        email = input('E-mail: ')

        telefone = input('Telefone: ')
        
        datadia = input('Dia do nascimento: ')
        datames = input('Mês do nascimento: ')
        dataano = input('Ano do nascimento: ')

        clientes[login] = [nome, login, senha, email, telefone, f'{datadia}/{datames}/{dataano}']
        
        resposta = input('Deseja cadastrar mais um usuário? [S/N] ')
        while resposta not in 'NnSs':
            print('\033[31mERRO! ESCOLHA UM OPÇÃO VÁLIDA!\033[m')
            resposta = input('Deseja cadastrar mais um usuário? [S/N] ')

        if resposta in 'Nn':
            break
    cabecalho('Cliente(s) cadastrado com sucesso!')


def cadastro_endereco():
    login = input('Login: ')
    senha = input('Senha: ')
    
    try:
        
        cliente = clientes[login]
        if senha != cliente[2]:
            print('=> \033[31mSenha incorreta!\033[m')
            return
    except:
        print('=> \033[33mCliente não cadastrado!\033[m')
        return 
        
    rua = input('Rua: ')

    numero = input('Número: ')
        
    complemento = input('Complemento: ')

    bairro = input('Bairro: ')

    cidade = input('Cidade: ')

    cep = input('CEP: ')
    
    ponto_referencia = input('Ponto de Referência: ')

    clientes[login].append([rua, numero, complemento, bairro, cidade, cep, ponto_referencia])

    cabecalho('Endereço cadastrado com sucesso!')
