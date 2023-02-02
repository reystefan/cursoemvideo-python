preco_atual = float(input('Preço atual do produto: '))
preco_desconto = preco_atual - (preco_atual * (5 / 100))

print(f'O preço do produto com 5% de desconto é {preco_desconto:.2f}')