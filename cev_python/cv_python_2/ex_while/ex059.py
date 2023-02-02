from time import sleep
valor_1 = None
valor_2 = None
opcao = None


while opcao != 5:
    if valor_1 is None:
        valor_1 = int(input('Digite um numero: '))
        valor_2 = int(input('Digite outro numero: '))

    sleep(1)
    opcao = int(input('''    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    Digite sua opção: '''))

    if opcao == 1:
        soma = valor_1 + valor_2
        print(f'{valor_1} + {valor_2} = {soma}')

    elif opcao == 2:
        produto = valor_1 * valor_2
        print(f'{valor_1} * {valor_2} = {produto}')

    elif opcao == 3:
        if valor_1 > valor_2:
            print(f'O {valor_1 = } é maior que {valor_2 = }')
        elif valor_2 > valor_1:
            print(f'O {valor_2 = } é maior que o {valor_1 = }')
        else:
            print(f'Os valores {valor_1 = } e {valor_2 = } são iguais.')
    elif opcao == 4:
        valor_1 = int(input('Digite um numero: '))
        valor_2 = int(input('Digite outro número: '))

    elif opcao < 1 or opcao > 5:
        print('Opção inválida. Tente novamente.')
    


print('Fim da execução.')