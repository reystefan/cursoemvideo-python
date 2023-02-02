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


def leiaFloat(strg):
    while True:
        try:
            v = float(input(strg))
        except (ValueError, TypeError):
            print('ERRO. Digite um número decimal válido.')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return v


n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número decimal: ')
print(f'O valor inteiro foi {n} e o real foi {n2}')
