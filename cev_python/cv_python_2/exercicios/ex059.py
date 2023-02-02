from time import sleep

sair = False
valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))

while sair is not True:
    opcao = int(input('''Escolha uma das opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Qual sua opção? '''))

    if opcao == 5:
        print('Finalizando. . .')
        sair = True
    elif opcao == 1:
        soma = valor_1 + valor_2
        print(f'A soma {valor_1} + {valor_2} é {soma}')
    elif opcao == 2:
        produto = valor_1 * valor_2
        print(f'A multiplicação {valor_1} * {valor_2} é {produto}')
    elif opcao == 3:
        if valor_1 > valor_2:
            print(f'O valor {valor_1} é maior que {valor_2}')
        elif valor_2 > valor_1:
            print(f'O valor {valor_2} é maior que {valor_1}')
        else:
            print(f'Os valores são iguais: {valor_1} = {valor_2}')
    elif opcao == 4:
        valor_1 = int(input('Digite um valor: '))
        valor_2 = int(input('Digite outro valor: '))
    
    sleep(1)

print('Fim do programa.')

