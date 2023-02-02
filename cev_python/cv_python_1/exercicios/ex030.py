numero = float(input('Digite um número qualquer: '))

if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')

#OU
print(f'O número {numero} é par!!!' if numero % 2 == 0 else f'O número \
{numero} é ímpar!!!')