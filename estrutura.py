def leia_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha():
    return '=' * 40


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'[{c}] {item}')
        c += 1
    print(linha())
    opc = leia_int('Sua Opção: ')
    return opc
