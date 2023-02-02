def leiaInt(strg=''):
    while True:
        v = input(strg)
        if v.isnumeric():
            v = int(v)
            return v
        else:
            print('ERRO. Digite um número inteiro válido.')      


n = leiaInt('Digite um numero: ')
print(f'Você digitou o número {n}')
