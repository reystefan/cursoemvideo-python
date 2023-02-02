from random import randint

print('Par ou ímpar \n')

while True:
    numero = int(input('Digite um número: '))

    while True:
        opcao = input('Par ou ímpar? (P ou I): ').strip().upper()
        if opcao == 'P' or opcao == 'I':
            break
        else:
            print('Por favor, digite uma opção válida.')
    
    num_computador = randint(0, 10)
    soma = num_computador + numero
    print(f'Jogador: {numero} e {opcao}')
    print(f'Computador: {num_computador} e', end= ' I\n' if opcao == 'P' else ' P\n')
    print(f'Soma: {soma}')

    if opcao == 'P':
        if soma % 2 != 0:
            print('Jogador PERDEU!\n')
            break
        else:
            print('Jogador VENCEU!\n')

    elif opcao == 'I':
        if soma % 2 == 0:
            print('Jogador PERDEU!\n')
            break 
        else:
            print('Jogador VENCEU!\n')
    
