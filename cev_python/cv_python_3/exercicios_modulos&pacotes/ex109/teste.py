import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatar(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.formatar(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')