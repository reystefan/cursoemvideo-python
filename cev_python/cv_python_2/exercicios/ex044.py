print(f'{"LOJAS PEREIRA":=^40}')

preco = float(input('Preço normal: '))
forma_pagamento = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque.
[ 2 ] à vista cartão
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.
Sua opção: """))
parcelas = None
novo_preco = None
valor_parcela = None

if forma_pagamento == 1: #  Á vista dinheiro/cheque 10% desconto
    novo_preco = preco - (preco * 0.1)
    print(f'O valor normal do produto é {preco:.2f} e com 10% de desconto ficou {novo_preco:.2f}')
elif forma_pagamento == 2:  #  Á vista cartão 5% desconto
    novo_preco = preco - (preco * 0.05)
    print(f'O valor normal do produto é {preco:.2f} e com 5% de desconto ficou {novo_preco:.2f}')
elif forma_pagamento == 3:  #  2x no cartão preço normal.
    valor_parcela = preco / 2
    print(f'O preço será de {preco:.2f}, parcelado em 2x ficará {valor_parcela:.2f} por mês.')
elif forma_pagamento == 4:  #  3x ou mais no cartão 20% de juros.
    parcelas = int(input('Quantas parcelas: '))
    if parcelas >= 3:
        juros = preco * 0.2
        novo_preco = preco + juros
        valor_parcela = novo_preco / parcelas
        print(f'O preço normal é R${preco:.2f}. Parcelado em {parcelas}x,'
        f' terá um juros de R${juros:.2f}. Preço total: R${novo_preco:.2f}. Mensalidade: R${valor_parcela:.2f} ')
    else:
        print('Para parcelas menores que 3x temos outras formas de pagamento. Por favor, escolha outra opção.')
else:
    print('Escolha uma opção válida.')
