qtd_divisoes = 0
numero = int(input('Digite um número: '))

print(f'O número {numero} é divisível por: ')
for c in range(1, numero + 1):
    if numero % c == 0:
        qtd_divisoes += 1
        print(c, end=' → ' if c < numero else '\n')

print(f'Ele foi dividido {qtd_divisoes} vezes ', end='')

if qtd_divisoes == 2:
    print('e por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')

