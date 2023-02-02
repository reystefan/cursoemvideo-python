# numero = input('Digite um número inteiro: ')
# numero_int = int(numero)
# binario = ''

# while numero_int > 2:
#     resto_str = str(numero_int % 2)
#     binario += resto_str
#     numero_int = numero_int // 2
# if numero_int <= 2:
#     resto_str = str(numero_int % 2)
#     numero_int = numero_int // 2
#     numero_str = str(numero_int)
#     binario += resto_str + numero_str  

# binario = binario[::-1]
# print(f'O número {numero} em binário é: {binario}')

numero = int(input('Digite um número inteiro: '))
base = int(input('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL

Sua opção: '''))

if base == 1:
    print(f'{numero} convertido para binário é igual a {bin(numero)[2:]}')
elif base == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)[2:]}')
elif base == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Base inválida. Tente novamente.')

