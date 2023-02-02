import moeda

preco = float(input('Preço: R$'))
print(f'O preço R${preco} aumentado em 10% é R${moeda.aumentar(preco, 10)}')
print(f'O preço R${preco} diminuído em 10% é R${moeda.diminuir(preco, 10)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'A metade de R${preco} é {moeda.metade(preco)}')

