print('Sequencia de Fibonacci com "n" elementos')

qtd_elementos = int(input('Digite um número: '))
valor_1 = 0
valor_2 = 1
contagem = 2

if qtd_elementos > 2:
    print(f'{valor_1} → {valor_2}', end='')
elif qtd_elementos == 2:
    print(f'{valor_1} → {valor_2}')
    contagem = 2
elif qtd_elementos == 1:
    print(f'{valor_1}')
    contagem = 1

while contagem < qtd_elementos:
    valor_3 = valor_1 + valor_2
    print(f' → {valor_3}', end='')
    valor_1 = valor_2
    valor_2 = valor_3
    contagem += 1