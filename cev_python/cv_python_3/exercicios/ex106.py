def pyHELP():
    from time import sleep
    while True:
        print('~'*30)
        print(f'{"SISTEMA DE AJUDA pyHELP":^30}')
        print('~'*30)
        opc = input('Função ou Biblioteca > ')

        if opc.strip().upper() == 'FIM':
            print('~'*(len("ATÉ LOGO!")+4))
            print(f'{"ATÉ LOGO!":^{len("ATÉ LOGO!")+4}}')
            print('~'*(len("ATÉ LOGO!")+4))
            break
        else:
            print('~'*(len(f"Acesando o manual do comando '{opc}'")+4))
            print(f"  Acesando o manual do comando '{opc}'")
            print('~'*(len(f"Acesando o manual do comando '{opc}'")+4))
            sleep(1)
            help(opc)
            print()
            sleep(1)


    
pyHELP()