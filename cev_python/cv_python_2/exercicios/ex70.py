print('-'*40)
print(f"{'LOJA KABUM':^40}")
print('-'*40)

nome_mais_barato = ''
preco_mais_barato = tot_valor = tot_maior_mil = 0

while True:
    nome_produto = input('Nome do produto: ').strip().title()
    preco = float(input('Preço do produto: '))

    if tot_valor == 0 or preco < preco_mais_barato:
        nome_mais_barato = nome_produto
        preco_mais_barato = preco

    tot_valor += preco

    # if preco < preco_mais_barato:
    #     preco_mais_barato = preco             ## Mesmos comandos de um if ja existente
    #     nome_mais_barato = nome_produto       ## Nesse caso, basta inserir um 'or' e adicionar a condição do segundo if que possui os mesmos comandos

    if preco > 1000:
        tot_maior_mil += 1


    while True:
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()
        if resposta == 'S' or resposta == 'N':
            break
        else:
            print('Resposta inválida, tente novamente.\n')

    if resposta == 'N':
        print('Finalizando. . . \n')
        break

print(f'Valor total da compra: R${tot_valor:.2f}')
print(f'Produtos com valor maior que R$1000,00: {tot_maior_mil}')
print(f'Nome do produto mais barato: {nome_mais_barato}')
print(f'Valor do produto mais barato: {preco_mais_barato}')