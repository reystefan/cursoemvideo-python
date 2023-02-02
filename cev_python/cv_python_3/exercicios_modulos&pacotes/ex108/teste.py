import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatar(preco)} é {moeda.formatar(moeda.metade(preco))}')
print(f'O dobro de {moeda.formatar(preco)} é {moeda.formatar(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.formatar(moeda.aumentar(preco, 10))}')