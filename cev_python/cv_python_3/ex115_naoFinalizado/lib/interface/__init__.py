def titulo(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)


def leiaInt(strg):
    while True:
        try:
            v = int(input(strg))
        except (ValueError, TypeError):
            print('ERRO. Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return v

        
def menu(lst):
    titulo('MENU PRINCIPAL')
    for pos, op in enumerate(lst):
        print(f'{pos+1} - {op}.') 
    print('-'*40)
    opc = leiaInt('Sua opção: ')
    return opc